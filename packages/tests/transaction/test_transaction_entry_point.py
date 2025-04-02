import pytest

from python_condor import TransactionEntryPoint


# ===== entrypoint_call =====
entrypoint_call = TransactionEntryPoint("Call")


def test_entrypoint_call_to_bytes():
    result = entrypoint_call.to_bytes().hex()
    assert result == "010000000000000000000100000000"


def test_entrypoint_call_to_json():
    result = entrypoint_call.to_json()
    assert result == {'entry_point': 'Call'}


# ===== entrypoint_custom =====
entrypoint_custom = TransactionEntryPoint("Custom", "test2")


def test_entrypoint_custom_to_bytes():
    result = entrypoint_custom.to_bytes().hex()
    assert result == "020000000000000000000100010000000a00000001050000007465737432"


def test_entrypoint_custom_to_json():
    result = entrypoint_custom.to_json()
    assert result == {'entry_point': {'Custom': "test2"}}


# ===== entrypoint_Transfer =====
entrypoint_transfer = TransactionEntryPoint("Transfer")


def test_entrypoint_transfer_to_bytes():
    result = entrypoint_transfer.to_bytes().hex()
    assert result == "010000000000000000000100000002"


def test_entrypoint_transfer_to_json():
    result = entrypoint_transfer.to_json()
    assert result == {'entry_point': 'Transfer'}


# ===== entrypoint_Add_Bid =====
entrypoint_add_bid = TransactionEntryPoint("Add_Bid")


def test_entrypoint_add_bid_to_bytes():
    result = entrypoint_add_bid.to_bytes().hex()
    assert result == "010000000000000000000100000003"


def test_entrypoint_add_bid_to_json():
    result = entrypoint_add_bid.to_json()
    assert result == {'entry_point': 'Add_Bid'}


# ===== entrypoint_Withdraw_Bid =====
entrypoint_withdraw_bid = TransactionEntryPoint("Withdraw_Bid")


def test_entrypoint_withdraw_bid_to_bytes():
    result = entrypoint_withdraw_bid.to_bytes().hex()
    assert result == "010000000000000000000100000004"


def test_entrypoint_withdraw_bid_to_json():
    result = entrypoint_withdraw_bid.to_json()
    assert result == {'entry_point': 'Withdraw_Bid'}


# ===== entrypoint_Delegate =====
entrypoint_delegate = TransactionEntryPoint("Delegate")


def test_entrypoint_delegate_to_bytes():
    result = entrypoint_delegate.to_bytes().hex()
    assert result == "010000000000000000000100000005"


def test_entrypoint_delegate_to_json():
    result = entrypoint_delegate.to_json()
    assert result == {'entry_point': 'Delegate'}


# ===== entrypoint_Undelegate =====
entrypoint_undelegate = TransactionEntryPoint("Undelegate")


def test_entrypoint_undelegate_to_bytes():
    result = entrypoint_undelegate.to_bytes().hex()
    assert result == "010000000000000000000100000006"


def test_entrypoint_undelegate_to_json():
    result = entrypoint_undelegate.to_json()
    assert result == {'entry_point': 'Undelegate'}


# ===== entrypoint_Redelegate =====
entrypoint_redelegate = TransactionEntryPoint("Redelegate")


def test_entrypoint_redelegate_to_bytes():
    result = entrypoint_redelegate.to_bytes().hex()
    assert result == "010000000000000000000100000007"


def test_entrypoint_redelegate_to_json():
    result = entrypoint_redelegate.to_json()
    assert result == {'entry_point': 'Redelegate'}


# ===== entrypoint_Activate_Bid =====
entrypoint_activate_bid = TransactionEntryPoint("Activate_Bid")


def test_entrypoint_activate_bid_to_bytes():
    result = entrypoint_activate_bid.to_bytes().hex()
    assert result == "010000000000000000000100000008"


def test_entrypoint_activate_bid_to_json():
    result = entrypoint_activate_bid.to_json()
    assert result == {'entry_point': 'Activate_Bid'}


# ===== entrypoint_ChangePublicKey =====
entrypoint_change_publickey = TransactionEntryPoint("ChangePublicKey")


def test_entrypoint_change_publickey_to_bytes():
    result = entrypoint_change_publickey.to_bytes().hex()
    assert result == "010000000000000000000100000009"


def test_entrypoint_change_publickey_to_json():
    result = entrypoint_change_publickey.to_json()
    assert result == {'entry_point': 'ChangePublicKey'}


# === check entrypoint out of range==
def test_entrypoint_out_of_range():
    with pytest.raises(ValueError, match=r"Invalid input: somegthingelse. Allowed values are: \('Call', 'Custom', 'Transfer', 'Add_Bid', 'Withdraw_Bid', 'Delegate', 'Undelegate', 'Redelegate', 'Activate_Bid', 'ChangePublicKey'\)"):
        _ = TransactionEntryPoint("somegthingelse")


# === check entrypoint name empty for Custom==
def test_entrypoint_out_of_range():
    with pytest.raises(ValueError, match="Entrypoint name cannot be empty for Custom."):
        _ = TransactionEntryPoint("Custom")
