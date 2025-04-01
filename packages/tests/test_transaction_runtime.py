import pytest

from python_condor import TransactionRuntime


# ===== transaction runtime v1 =====
transaction_runtime_v1 = TransactionRuntime()


def test_transaction_runtime_to_bytes():
    result = transaction_runtime_v1.to_bytes().hex()
    assert result == "010000000000000000000100000000"


def test_transaction_runtime_to_json():
    result = transaction_runtime_v1.to_json()
    assert result == {'runtime': 'VmCasperV1'}


# ===== check runtime rather than v1 =====
def test_transaction_runtime_v2():
    with pytest.raises(ValueError, match="Invalid input VmCasperV2. Allowed values are: VmCasperV1"):
        _ = TransactionRuntime("VmCasperV2")
