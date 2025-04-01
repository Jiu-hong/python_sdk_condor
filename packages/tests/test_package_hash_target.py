import pytest

from python_condor import PackageHashTarget


# ===== PackageHashTarget without version =====
target_no_version = PackageHashTarget(
    "VmCasperV1", "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")


def test_targetnoversion_to_bytes():
    result = target_no_version.to_bytes().hex()
    assert result == "0300000000000000000001000100000002003d0000004c00000001030000000000000000000100010000000200210000002200000002cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b5600010000000000000000000100000000"


def test_targetnoversion_to_json():
    result = target_no_version.to_json()
    assert result == {'target': {'Stored': {'id': {'ByPackageHash': {
        'addr': 'cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56', 'version': None}}, 'runtime': 'VmCasperV1'}}}


# # ===== PackageHashTarget with version =====
target_with_version = PackageHashTarget("VmCasperV1",
                                        "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56", 1)


def test_targetwithversion_to_bytes():
    result = target_with_version.to_bytes().hex()
    assert result == "030000000000000000000100010000000200410000005000000001030000000000000000000100010000000200210000002600000002cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b560101000000010000000000000000000100000000"


def test_targetwithversion_to_json():
    result = target_with_version.to_json()
    assert result == {'target': {'Stored': {'id': {'ByPackageHash': {
        'addr': 'cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56', 'version': 1}}, 'runtime': 'VmCasperV1'}}}


# === check format incorrect
def test_packagehash_regex_pattern_not_match():
    with pytest.raises(ValueError, match=r"package-hash should only contain alphabet and number\(64 length\)"):
        _ = PackageHashTarget(
            "VmCasperV1", "123-0")
