from python_condor import CLKey


# ===== CLKey bid_addr =====

clkey_bid_addr = CLKey(
    "bid-addr-03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c")


def test_clkey_serialize():
    result = clkey_bid_addr.serialize().hex()
    assert result == "0f03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c"


def test_clkey_string_value():
    result = clkey_bid_addr.value()
    assert result == "bid-addr-03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c"


def test_clkey_cl_value():
    result = clkey_bid_addr.cl_value()
    assert result == "420000000f03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c0b"


def test_clkey_to_json():
    result = clkey_bid_addr.to_json()
    assert result == "Key"
