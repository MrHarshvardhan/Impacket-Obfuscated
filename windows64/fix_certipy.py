import os

# Patch errors.py
errors_path = "certipy/lib/errors.py"
with open(errors_path, 'r') as f:
    content = f.read()

# Replace the impacket import
content = content.replace(
    "from impacket import hresult_errors",
    "try:\n    from impacket import hresult_errors\nexcept ImportError:\n    hresult_errors = None\n    class DummyHRESULT:\n        @staticmethod\n        def check_error_for_hresult(code):\n            return None\n    hresult_errors = DummyHRESULT()"
)

with open(errors_path, 'w') as f:
    f.write(content)

print("Patched errors.py")
