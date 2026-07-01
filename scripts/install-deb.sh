#!/usr/bin/env bash
# scripts/install-deb.sh — build and install the dan-glasses-daemons .deb
#
# Usage:
#   ./scripts/install-deb.sh                # build + install (sudo if not root)
#   ./scripts/install-deb.sh build          # build only, output to ../packaging/dist
#   ./scripts/install-deb.sh start          # enable + start all units (post-install)
#   ./scripts/install-deb.sh stop           # stop + disable all units
#   ./scripts/install-deb.sh status         # show all unit states
#   ./scripts/install-deb.sh uninstall      # apt remove the package
#
# Requires: dpkg-dev, debhelper, dh-python, fakeroot (or root).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEB_DIR="$ROOT/packaging/debian"
DIST_DIR="$ROOT/packaging/dist"
PKG_NAME="dan-glasses-daemons"

# Temporary build root: copy only what .install references, so dh_install
# doesn't see scripts/ or tests/ or node_modules.
BUILD_ROOT="$(mktemp -d -t danglasses-deb.XXXXXX)"
trap 'rm -rf "$BUILD_ROOT"' EXIT

cp -r "$ROOT/Services" "$BUILD_ROOT/Services"
cp -r "$ROOT/packaging/systemd" "$BUILD_ROOT/packaging-systemd"
cp -r "$DEB_DIR" "$BUILD_ROOT/debian"
# Patch the .install file to refer to the renamed systemd dir.
sed -i 's|^packaging/systemd/|packaging-systemd/|' "$BUILD_ROOT/debian/dan-glasses-daemons.install"
chmod +x "$BUILD_ROOT/debian/rules"
chmod +x "$BUILD_ROOT/debian/dan-glasses-daemons.postinst" \
         "$BUILD_ROOT/debian/dan-glasses-daemons.prerm" \
         "$BUILD_ROOT/debian/dan-glasses-daemons.postrm"

build_deb() {
  command -v dpkg-buildpackage >/dev/null 2>&1 || {
    echo "ERROR: dpkg-buildpackage not found. Install: apt install dpkg-dev debhelper dh-python fakeroot" >&2
    exit 1
  }
  mkdir -p "$DIST_DIR"
  cd "$BUILD_ROOT"
  # -us -uc = don't sign source/changes. -b = binary only.
  dpkg-buildpackage -us -uc -b -a "$(dpkg --print-architecture)"
  # Move artifacts to packaging/dist
  find .. -maxdepth 1 -name "${PKG_NAME}_*.deb" -exec mv {} "$DIST_DIR/" \;
  find .. -maxdepth 1 -name "${PKG_NAME}_*.changes" -exec mv {} "$DIST_DIR/" \;
  cd - >/dev/null
  echo ""
  echo "Built:"
  ls -la "$DIST_DIR/"*.deb 2>/dev/null
}

install_deb() {
  local deb
  deb="$(ls -1t "$DIST_DIR"/${PKG_NAME}_*.deb 2>/dev/null | head -1)"
  if [ -z "$deb" ]; then
    echo "No .deb in $DIST_DIR. Run: $0 build" >&2
    exit 1
  fi
  echo "Installing $deb ..."
  if [ "$(id -u)" -eq 0 ]; then
    DEBIAN_FRONTEND=noninteractive apt-get install -y "$deb"
  else
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y "$deb"
  fi
}

UNITS=(dan-glasses-audiod dan-glasses-perceptiond dan-glasses-memoryd
       dan-glasses-toold dan-glasses-ttsd dan-glasses-os-toold)

unit_op() {
  local op="$1"
  for u in "${UNITS[@]}"; do
    if [ -d /run/systemd/system ]; then
      sudo systemctl "$op" "$u.service" || true
    fi
  done
}

case "${1:-install}" in
  build)
    build_deb
    ;;
  install|"")
    build_deb
    install_deb
    echo ""
    echo "Next: $0 start"
    ;;
  start)
    unit_op enable
    unit_op start
    sudo systemctl --system daemon-reload || true
    $0 status
    ;;
  stop)
    unit_op stop
    unit_op disable
    ;;
  status)
    for u in "${UNITS[@]}"; do
      printf "%-32s " "$u"
      systemctl is-active "$u.service" 2>/dev/null || echo "inactive"
    done
    ;;
  uninstall)
    if [ "$(id -u)" -eq 0 ]; then
      DEBIAN_FRONTEND=noninteractive apt-get remove -y "$PKG_NAME" || true
    else
      sudo DEBIAN_FRONTEND=noninteractive apt-get remove -y "$PKG_NAME" || true
    fi
    ;;
  *)
    echo "Usage: $0 [build|install|start|stop|status|uninstall]" >&2
    exit 2
    ;;
esac
