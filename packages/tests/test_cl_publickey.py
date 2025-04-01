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


# === check length is not 1
def test_clpublickey_regex_pattern_not_match():
    with pytest.raises(ValueError, match=r"publickey should be 01xxx\(64 length\) or 02xxx\(66 length\)"):
        _ = CLPublicKey(
            "123456")
