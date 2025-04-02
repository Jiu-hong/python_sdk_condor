import pytest

from python_condor import SessionContractHash
from python_condor.cl_values.cl_number import CLU256
from python_condor.cl_values.cl_string import CLString


# ===== SessionContractHash =====
contract_hash = "596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b"
entrypoint = "apple"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
# runtime_args = {}
session_contract_hash = SessionContractHash(
    contract_hash, entrypoint, runtime_args)
# session_hexstring = session_packagehash.to_bytes()


def test_session_contract_hash_to_bytes():
    result = session_contract_hash.to_bytes().hex()
    assert result == "01596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b050000006170706c6502000000040000006172673102000000017b070400000061726732090000000500000068656c6c6f0a"


def test_session_contract_hash_to_json():
    result = session_contract_hash.to_json()
    assert result == {'session': {'StoredContractByHash': {'hash': '596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b', 'entry_point': 'apple', 'args': [
        ('arg1', {'cl_type': 'U256', 'bytes': '017b', 'parsed': 123}), ('arg2', {'cl_type': 'String', 'bytes': '0500000068656c6c6f', 'parsed': 'hello'})]}}}


# === check contract-hash incorrect length==
def test_session_contract_hash_incorrect_hash_length():
    contract_hash = "1234abcd"
    entrypoint = "apple"
    runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
    with pytest.raises(ValueError, match=r"contract-hash should only contain alphabet and number\(64 length\)"):
        _ = SessionContractHash(
            contract_hash, entrypoint, runtime_args)


# === check entrypoint incorrect type==
def test_session_contract_hash_incorrect_entry_type():
    contract_hash = "596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b"
    entrypoint = 123
    runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
    with pytest.raises(TypeError, match="The entrypoint should be of type str"):
        _ = SessionContractHash(
            contract_hash, entrypoint, runtime_args)
