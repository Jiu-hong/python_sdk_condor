from python_condor import TransactionNativeTarget


# ===== Native target =====
target_native = TransactionNativeTarget()


def test_target_native_to_bytes():
    result = target_native.to_bytes().hex()
    assert result == "010000000000000000000100000000"


def test_target_native_to_json():
    result = target_native.to_json()
    assert result == {'target': "Native"}
