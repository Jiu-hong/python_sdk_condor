from result import Err, Ok
import re
from .call_table_serialization import CalltableSerialization

REGX_PUBLICKEY = "(01[0-9a-zA-Z]{64})|(02[0-9a-zA-Z]{66})"
REGX_HASH = "([0-9a-z]{64})"


def check_format(regx, data) -> bool:
    pattern = re.compile(regx)
    result = pattern.fullmatch(data)
    return isinstance(result, re.Match)


def check_clkey_format(clkey):
    if not clkey.startswith(("account-hash-", "hash-", "uref-")):
        raise ValueError(
            "clkey should start with 'account-hash-, hash-, uref-...'")

    # key:account-hash-xxx
    if clkey.startswith("account-hash"):
        check_account_hash_format(clkey)
    # key:hash-xxx
    elif clkey.startswith("hash-"):
        if not check_format(REGX_HASH, clkey.split("-")[1]):
            raise ValueError(
                "key::hash value should be 64 length only containing alphabet and number")
    # key:uref-xxx
    elif clkey.startswith("uref-"):
        check_purse_format(clkey)


def check_contract_package_format(contract_package):
    if not contract_package.startswith("contract-package-"):
        raise ValueError(
            "contract-package should start with 'contract-package-'")
    if not check_format(REGX_HASH, contract_package.split("-")[2]):
        raise ValueError(
            "contract-package value should be 64 length only containing alphabet and number")


def check_deploy_hash_format(deploy_hash):
    if deploy_hash is None:
        raise ValueError("transaction/deploy_hash shouldn't be empty")
    if not check_format(REGX_HASH, deploy_hash):
        raise ValueError(
            "transaction/deploy_hash should be 64 length only containing alphabet and number")


def check_account_hash_format(account_hash):
    if not account_hash.startswith("account-hash-"):
        raise ValueError("account hash should start with 'account-hash-'")
    if not check_format(REGX_HASH, account_hash.split("-")[2]):
        raise ValueError(
            "account-hash value should be 64 length only containing alphabet and number")


def check_purse_format(purse):
    if not purse.startswith("uref-"):
        raise ValueError("purse should start with 'uref-'")
    if not purse.endswith(('000', '001', '002', '003', '004', '005', '006', '007')):
        raise ValueError("uref should end with '000 - 007'")
    if not check_format(REGX_HASH, purse.split("-")[1]):
        raise ValueError(
            "account-hash value should be 64 length only containing alphabet and number")


def check_block_format(block_id):
    if isinstance(block_id, str):
        if not check_format(REGX_HASH, block_id):
            raise ValueError(
                "block-hash value should be 64 length only containing alphabet and number")


def check_root_state_hash_format(state_root_hash):
    if state_root_hash is not None:
        if not isinstance(state_root_hash, str):
            raise TypeError("state_root_hash should be type str")
        if not check_format(REGX_HASH, state_root_hash):
            raise ValueError(
                "state_root_hash should be 64 length only containing alphabet and number")


def check_public_key_format(public_key):
    if not check_format(REGX_PUBLICKEY, public_key):
        raise ValueError(
            "publickey should be 01xxx(64 length) or 02xxx(66 length)")


def serialize_string(data) -> bytes:
    content = bytearray(data, encoding="utf-8")
    bytes_len = int(len(content)).to_bytes(4, byteorder='little')
    return bytes_len+content


def deep_value_v2(self):
    result = ""
    if isinstance(self, int | str):
        result = self
        if isinstance(self, str):
            result = f'{self}'
    elif isinstance(self, tuple | list):
        # check if CLResult
        if isinstance(self, tuple) and isinstance(self[-1], bool):
            if self[-1] == True:  # OK value
                result = {'Ok': deep_value_v2(self[0])}
            else:  # err value
                result = {'Err': deep_value_v2(self[1])}
            return result
        # check if cloption none
        if isinstance(self, tuple) and self[0] is None:
            return
        result = [deep_value_v2(x) for x in self]
        if isinstance(self, tuple):
            result = tuple(result)
    elif isinstance(self, dict):
        result = []
        for key_value in self.items():
            item = {'key': deep_value_v2(
                key_value[0]), 'value': deep_value_v2(key_value[1])}
            result.append(item)
    elif isinstance(self, Ok):
        result = deep_value_v2(self.ok_value)
    elif isinstance(self, Err):
        result = deep_value_v2(self.err_value)
    elif self is None:
        result = None
    else:
        result = deep_value_v2(self.data)
    return result
