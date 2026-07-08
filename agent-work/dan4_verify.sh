#!/usr/bin/env bash
# Full verification matrix for DAN-4 deliverables
set +e
ROOT="/home/workspace/dan-glasses"

echo "=== memoryd ==="
cd "$ROOT/Services/memoryd"
timeout 120 python3 -m pytest test_memoryd.py test_boot_window.py test_wizard_roundtrip.py -q --no-header 2>&1 | tail -3

echo "=== toold ==="
cd "$ROOT/Services/toold"
timeout 60 python3 -m pytest test_toold.py -q --no-header 2>&1 | tail -3

echo "=== ttsd ==="
cd "$ROOT/Services/ttsd"
timeout 60 python3 -m pytest test_ttsd.py -q --no-header 2>&1 | tail -3

echo "=== dan-glasses-app ==="
cd "$ROOT/Services/dan-glasses-app"
for f in test_health_aggregator.py test_proxy.py test_public_proxy_roundtrip.py test_wizard_proxy_roundtrip.py test_services_ts_refactor.py; do
  echo "  $f"
  timeout 30 python3 -m pytest "$f" -q --no-header 2>&1 | tail -1
done
echo "  test_proxies.py (script)"
timeout 30 python3 test_proxies.py 2>&1 | tail -1
echo "  test_perceptiond_roundtrip.py (script)"
timeout 30 python3 test_perceptiond_roundtrip.py 2>&1 | tail -1
echo "  test_perceptiond_proxy.py"
timeout 60 python3 -m pytest test_perceptiond_proxy.py -q --no-header 2>&1 | tail -1
echo "  test_ws_upgrade.py"
timeout 60 python3 -m pytest test_ws_upgrade.py -q --no-header 2>&1 | tail -1
