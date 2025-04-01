import pytest

from python_condor import PackageNameTarget


# ===== PackageNameTarget without version =====

target_no_version = PackageNameTarget("VmCasperV1", "my_hash")


def test_targetnoversion_to_bytes():
    result = target_no_version.to_bytes().hex()
    assert result == "0300000000000000000001000100000002002800000037000000010300000000000000000001000100000002000c0000000d00000003070000006d795f6861736800010000000000000000000100000000"


def test_targetnoversion_to_json():
    result = target_no_version.to_json()
    assert result == {'target': {'Stored': {'id': {'ByPackageName': {
        'name': 'my_hash', 'version': None}}, 'runtime': 'VmCasperV1'}}}


# ===== PackageNameTarget with version =====
target_with_version = PackageNameTarget("VmCasperV1", "my_hash", 1)


def test_targetwithversion_to_bytes():
    result = target_with_version.to_bytes().hex()
    assert result == "0300000000000000000001000100000002002c0000003b000000010300000000000000000001000100000002000c0000001100000003070000006d795f686173680101000000010000000000000000000100000000"


def test_targetwithversion_to_json():
    result = target_with_version.to_json()
    assert result == {'target': {'Stored': {'id': {'ByPackageName': {
        'name': 'my_hash', 'version': 1}}, 'runtime': 'VmCasperV1'}}}
