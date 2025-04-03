import pytest
from datetime import datetime

from python_condor import DeployHeader


# ===== DeployHeader =====
account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chain_name = "integration-test"
header = DeployHeader(account, chain_name,
                      datetime.fromisoformat('2025-03-26T03:11:48.829Z'), ttl=30, gas_price=1)


# === add_body_hash ===
def test_header_add_body_hash():
    assert not hasattr(header, "body_hash")
    header.add_body_hash(
        "7dca5f79b9d4c7e5fc0f15a34f22b9bb03ae1012071105ce499c2962c64d261d")
    assert header.body_hash is not None


# === to_bytes() ===
def test_header_to_bytes():
    result = header.to_bytes().hex()
    assert result == "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f55d486fd09501000040771b000000000001000000000000007dca5f79b9d4c7e5fc0f15a34f22b9bb03ae1012071105ce499c2962c64d261d0000000010000000696e746567726174696f6e2d74657374"


# ==== byteHash()
def test_header_byteHash():
    result = header.byteHash()
    assert result == "a0935128f23f700d2b5a87640830967d3a14ae6652a86faf7f77e04b26c536f2"


# ==== to_json()
def test_header_to_json():
    result = header.to_json()
    assert result == {'header': {'account': '017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5', 'timestamp': '2025-03-26T03:11:48.829Z', 'ttl': '30m',
                                 'gas_price': 1, 'body_hash': '7dca5f79b9d4c7e5fc0f15a34f22b9bb03ae1012071105ce499c2962c64d261d', 'dependencies': [], 'chain_name': 'integration-test'}}


# === check account pattern
def test_header_check_account_pattern():
    account = "xxxx"
    chain_name = "integration-test"
    with pytest.raises(ValueError, match=r"account should be 01xxx\(64 length\) or 02xxx\(66 length\)"):
        _ = DeployHeader(account, chain_name,
                         datetime.fromisoformat('2025-03-26T03:11:48.829Z'), ttl=30, gas_price=1)


# === check chain-name
def test_header_check_chain_name():
    account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
    chain_name = ""
    with pytest.raises(ValueError, match="The chain_name shouldn't be empty."):
        _ = DeployHeader(account, chain_name,
                         datetime.fromisoformat('2025-03-26T03:11:48.829Z'), ttl=30, gas_price=1)


# === check time
def test_header_time():
    account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
    chain_name = "integration-test"
    with pytest.raises(TypeError, match="time should be type datetime.datetime"):
        _ = DeployHeader(account, chain_name,
                         1234, ttl=30, gas_price=1)


# === check ttl
def test_header_ttl():
    account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
    chain_name = "integration-test"
    with pytest.raises(TypeError, match="ttl should be type int"):
        _ = DeployHeader(account, chain_name,
                         datetime.fromisoformat('2025-03-26T03:11:48.829Z'), ttl="30", gas_price=1)


# === check gas_price
def test_header_gas_price():
    account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
    chain_name = "integration-test"
    with pytest.raises(TypeError, match="gas_price should be type int"):
        _ = DeployHeader(account, chain_name,
                         datetime.fromisoformat('2025-03-26T03:11:48.829Z'), ttl=30, gas_price="1")
