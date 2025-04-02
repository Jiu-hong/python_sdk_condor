import pytest

from python_condor import TransactionSessionTarget


# ===== Session target install=True =====

module_bytes = "000102030405"
target_session_install = TransactionSessionTarget(
    "VmCasperV1", module_bytes, True)


def test_target_session_install_to_bytes():
    result = target_session_install.to_bytes().hex()
    assert result == "040000000000000000000100010000000200020000000300110000001b000000020101000000000000000000010000000006000000000102030405"


def test_target_session_install_to_json():
    result = target_session_install.to_json()
    assert result == {'target': {'Session': {'is_install_upgrade': True,
                                             'module_bytes': '000102030405', 'runtime': 'VmCasperV1'}}}


# # ===== Session target install=False =====
# module_bytes = "000102030405"
# target_session_no_install = TransactionSessionTarget(
#     "VmCasperV1", module_bytes, False)


# def test_target_session_no_install_to_bytes():
#     result = target_session_no_install.to_bytes().hex()
#     assert result == "040000000000000000000100010000000200020000000300110000001b000000020001000000000000000000010000000006000000000102030405"


# def test_target_session_no_install_to_json():
#     result = target_session_no_install.to_json()
#     assert result == {'target': {'Session': {'is_install_upgrade': False,
#                                              'module_bytes': '000102030405', 'runtime': 'VmCasperV1'}}}
