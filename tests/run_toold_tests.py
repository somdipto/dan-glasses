#!/usr/bin/env python3
"""Quick verification of toold core logic."""
import sys, os, tempfile
sys.path.insert(0, 'Services/toold')
import toold

# validate
assert toold.validate_shell_command('ls') == True
assert toold.validate_shell_command('echo hi; rm -rf /') == False
assert toold.validate_shell_command('echo hi && ls') == False
print('validate OK')

# registry round-trip
tmp = tempfile.mktemp(suffix='.json')
orig = toold.REGISTRY_PATH
toold.REGISTRY_PATH = tmp
toold.save_registry({'tools': [{'name': 'test_tool', 'enabled': True}]})
loaded = toold.load_registry()
assert loaded['tools'][0]['name'] == 'test_tool'
toold.REGISTRY_PATH = orig
os.unlink(tmp)
print('registry OK')

print('toold core logic: ALL PASSED')
