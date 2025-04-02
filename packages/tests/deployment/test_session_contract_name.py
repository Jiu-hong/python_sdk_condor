import pytest

from python_condor import SessionContractName, CLU256, CLString


# ===== SessionContractName =====

contract_name = "apple_contract"
entrypoint = "apple"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}

session_contract_name = SessionContractName(
    contract_name, entrypoint, runtime_args)


def test_session_contract_name_to_bytes():
    result = session_contract_name.to_bytes().hex()
    assert result == "020e0000006170706c655f636f6e7472616374050000006170706c6502000000040000006172673102000000017b070400000061726732090000000500000068656c6c6f0a"


def test_session_contract_name_to_json():
    result = session_contract_name.to_json()
    assert result == {'session': {'StoredContractByName': {'name': 'apple_contract', 'entry_point': 'apple', 'args': [
        ('arg1', {'cl_type': 'U256', 'bytes': '017b', 'parsed': 123}), ('arg2', {'cl_type': 'String', 'bytes': '0500000068656c6c6f', 'parsed': 'hello'})]}}}

# === check contract-name empty==


def test_session_contract_name_contract_name_empty():
    contract_name = ""
    entrypoint = "apple"
    runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
    with pytest.raises(ValueError, match="The contract name shouldn't be empty."):
        _ = SessionContractName(
            contract_name, entrypoint, runtime_args)


# === check entrypoint empty==
def test_session_contract_name_entrypoint_empty():
    contract_name = "apple_contract"
    entrypoint = ""
    runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
    with pytest.raises(ValueError, match="The entrypoint shouldn't be empty."):
        _ = SessionContractName(
            contract_name, entrypoint, runtime_args)

# # === check entrypoint incorrect type==
# def test_session_contract_name_incorrect_entry_type():
#     contract_name = "596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b"
#     entrypoint = 123
#     runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
#     with pytest.raises(TypeError, match="The entrypoint should be of type str"):
#         _ = SessionContractName(
#             contract_name, entrypoint, runtime_args)
