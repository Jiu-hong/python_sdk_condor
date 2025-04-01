import pytest

from python_condor import EntityTarget


# ===== EntityTarget =====
target = EntityTarget("VmCasperV1",
                      "b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6")


def test_targetnoversion_to_bytes():
    result = target.to_bytes().hex()
    assert result == "030000000000000000000100010000000200360000004500000001020000000000000000000100010000002100000000b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6010000000000000000000100000000"


def test_targetnoversion_to_json():
    result = target.to_json()
    assert result == {'target': {'Stored': {'id': {'ByHash': 'b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6'},
                                            'runtime': 'VmCasperV1'}}}


# === check format incorrect
def test_contracthash_regex_pattern_not_match():
    with pytest.raises(ValueError, match=r"contract-hash should only contain alphabet and number\(64 length\)"):
        _ = EntityTarget(
            "VmCasperV1", "123-0")
