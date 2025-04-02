import pytest

from python_condor import SessionPackageName, CLU256, CLString


# ===== SessionPackageName =====

package_name = "my_hash"
entrypoint = "apple"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}

session_package_name = SessionPackageName(
    package_name, None, entrypoint, runtime_args)


def test_session_package_name_to_bytes():
    result = session_package_name.to_bytes().hex()
    assert result == "04070000006d795f6861736800050000006170706c6502000000040000006172673102000000017b070400000061726732090000000500000068656c6c6f0a"


def test_session_package_name_to_json():
    result = session_package_name.to_json()
    assert result == {'session': {'StoredVersionedContractByName': {'name': 'my_hash', 'version': None, 'entry_point': 'apple', 'args': [
        ('arg1', {'cl_type': 'U256', 'bytes': '017b', 'parsed': 123}), ('arg2', {'cl_type': 'String', 'bytes': '0500000068656c6c6f', 'parsed': 'hello'})]}}}


# # === check package-name empty==
def test_session_package_name_package_name_empty():
    package_name = ""
    entrypoint = "apple"
    runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
    with pytest.raises(ValueError, match="The package name shouldn't be empty."):
        _ = SessionPackageName(
            package_name, None, entrypoint, runtime_args)


# === check entrypoint empty==
def test_session_package_name_entrypoint_empty():
    package_name = "apple_contract"
    entrypoint = ""
    runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
    with pytest.raises(ValueError, match="The entrypoint shouldn't be empty."):
        _ = SessionPackageName(
            package_name, None, entrypoint, runtime_args)
