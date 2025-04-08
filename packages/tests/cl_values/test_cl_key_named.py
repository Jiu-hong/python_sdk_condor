import pytest
from python_condor import CLKey


# ===== CLKey - named_key-entity-account =====
clkey_namedkey_entity_account = CLKey(
    "named-key-entity-account-928d914bdcad3ca269e750f63ed3615c5d3f615cf97dba87006fd9f979dacb3c-dde6f264c89fe385a5b07c26d77284d6fddabe79653c5ca25cec39a6363e6ec7")


def test_clkey_namedkey_entity_account_serialize():
    result = clkey_namedkey_entity_account.serialize().hex()
    assert result == "1401928d914bdcad3ca269e750f63ed3615c5d3f615cf97dba87006fd9f979dacb3cdde6f264c89fe385a5b07c26d77284d6fddabe79653c5ca25cec39a6363e6ec7"


def test_clkey_namedkey_entity_account_string_value():
    result = clkey_namedkey_entity_account.value()
    assert result == "named-key-entity-account-928d914bdcad3ca269e750f63ed3615c5d3f615cf97dba87006fd9f979dacb3c-dde6f264c89fe385a5b07c26d77284d6fddabe79653c5ca25cec39a6363e6ec7"


def test_clkey_namedkey_entity_account_cl_value():
    result = clkey_namedkey_entity_account.cl_value()
    assert result == "420000001401928d914bdcad3ca269e750f63ed3615c5d3f615cf97dba87006fd9f979dacb3cdde6f264c89fe385a5b07c26d77284d6fddabe79653c5ca25cec39a6363e6ec70b"


def test_clkey_namedkey_entity_account_to_json():
    result = clkey_namedkey_entity_account.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_namedkey_entity_account_hash_invalid():
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "named-key-entity-account-xx-xx")


def test_clkey_namedkey_entity_account_one_hash():
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address and a namedkey hash."):
        _ = CLKey(
            "named-key-entity-account-xx")


def test_clkey_namedkey_entity_account_three_hash():
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address and a namedkey hash."):
        _ = CLKey(
            "named-key-entity-account-xx-xx-xx")


def test_clkey_namedkey_entity_account_not_start_with_entity():
    with pytest.raises(ValueError, match="data should start with 'entity-"):
        _ = CLKey(
            "named-key-something-account-xx-xx")


# ===== CLKey - named_key-entity-contract =====
clkey_namedkey_entity_contract = CLKey(
    "named-key-entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b")


def test_clkey_namedkey_entity_contract_serialize():
    result = clkey_namedkey_entity_contract.serialize().hex()
    assert result == "14022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b"


def test_clkey_namedkey_entity_contract_string_value():
    result = clkey_namedkey_entity_contract.value()
    assert result == "named-key-entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b"


def test_clkey_namedkey_entity_contract_cl_value():
    result = clkey_namedkey_entity_contract.cl_value()
    assert result == "4200000014022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b0b"


def test_clkey_namedkey_entity_contract_to_json():
    result = clkey_namedkey_entity_contract.to_json()
    assert result == "Key"
