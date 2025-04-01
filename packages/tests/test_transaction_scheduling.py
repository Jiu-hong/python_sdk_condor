import pytest

from python_condor import TransactionScheduling

# ===== transaction scheduling =====
transaction_scheduling = TransactionScheduling()


def test_transaction_scheduling_to_bytes():
    result = transaction_scheduling.to_bytes().hex()
    assert result == "010000000000000000000100000000"


def test_transaction_scheduling_to_json():
    result = transaction_scheduling.to_json()
    assert result == {'scheduling': 'Standard'}


# ===== check scheduling rather than Standard =====
def test_transaction_scheduling_nostandard():
    with pytest.raises(ValueError, match="Invalid input: somethingelse. Valid allowed values: Standard"):
        _ = TransactionScheduling("somethingelse")
