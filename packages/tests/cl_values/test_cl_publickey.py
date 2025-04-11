import pytest

from python_condor import CLPublicKey


# ===== CLPublicKey ED25519=====

clpublickey = CLPublicKey(
    "0119bf44096984cdfe8541bac167dc3b96c85086aa30b6b6cb0c5c38ad703166e1")


def test_clpublickey_serialize():
    result = clpublickey.serialize().hex()
    assert result == "0119bf44096984cdfe8541bac167dc3b96c85086aa30b6b6cb0c5c38ad703166e1"


def test_clpublickey_string_value():
    result = clpublickey.value()
    assert result == "0119bf44096984cdfe8541bac167dc3b96c85086aa30b6b6cb0c5c38ad703166e1"


def test_clpublickey_cl_value():
    result = clpublickey.cl_value()
    assert result == "210000000119bf44096984cdfe8541bac167dc3b96c85086aa30b6b6cb0c5c38ad703166e116"


def test_clpublickey_to_json():
    result = clpublickey.to_json()
    assert result == "PublicKey"


def test_clpublickey_get_account_Ed25519():
    result = clpublickey.get_account_hash()
    assert result == "290ee54c1c974a8f90e3178eba65405b2d7af8392a65c629c145d0a0ee8bb1dd"


def test_clpublickey_get_account_secp256k1():
    secp256k1_clpublickey = CLPublicKey(
        "020233e54d818925bad633b837e0cece45f4e3d4498d0da04957047d3abd378679c7")
    result = secp256k1_clpublickey.get_account_hash()
    assert result == "5978e0e5aea2d9b13f5af353fb333b7084f950c0be0655ea93298d2b57a973f7"


# === check format
def test_clpublickey_regex_pattern_not_match():
    with pytest.raises(ValueError, match=r"Public key should be 01xxx\(64 length\) or 02xxx\(66 length\)"):
        _ = CLPublicKey(
            "123456")
