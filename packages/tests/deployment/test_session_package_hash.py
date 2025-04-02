import pytest

from python_condor import SessionPackageHash, CLU256, CLString


# ===== SessionPackageHash =====

package_name = "051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"
entrypoint = "apple"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}

session_package_name = SessionPackageHash(
    package_name, None, entrypoint, runtime_args)


def test_session_package_name_to_bytes():
    result = session_package_name.to_bytes().hex()
    assert result == "03051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef600050000006170706c6502000000040000006172673102000000017b070400000061726732090000000500000068656c6c6f0a"


def test_session_package_name_to_json():
    result = session_package_name.to_json()
    assert result == {'session': {'StoredVersionedContractByHash': {'hash': '051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6', 'version': None, 'entry_point': 'apple', 'args': [
        ('arg1', {'cl_type': 'U256', 'bytes': '017b', 'parsed': 123}), ('arg2', {'cl_type': 'String', 'bytes': '0500000068656c6c6f', 'parsed': 'hello'})]}}}

# # === check package_hash empty==


def test_session_package_name_package_name_empty():
    package_name = ""
    entrypoint = "apple"
    runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
    with pytest.raises(ValueError, match=r"package-hash should only contain alphabet and number\(64 length\)"):
        _ = SessionPackageHash(
            package_name, None, entrypoint, runtime_args)


# === check entrypoint empty==
def test_session_package_name_entrypoint_empty():
    package_name = "051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"
    entrypoint = ""
    runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
    with pytest.raises(ValueError, match="The entrypoint shouldn't be empty."):
        _ = SessionPackageHash(
            package_name, None, entrypoint, runtime_args)
