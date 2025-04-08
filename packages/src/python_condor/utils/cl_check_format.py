import re
from ..constants import BidAddrTag

REGX_PUBLICKEY = "(01[0-9a-zA-Z]{64})|(02[0-9a-zA-Z]{66})"
REGX_HASH = "([0-9a-z]{64})"
BID_ADDR_TAG = BidAddrTag()


def check_format(regx, data) -> bool:
    pattern = re.compile(regx)
    result = pattern.fullmatch(data)
    return isinstance(result, re.Match)


def check_account_hash_format(account_hash):
    if not account_hash.startswith("account-hash-"):
        raise ValueError("account hash should start with 'account-hash-'")
    if not check_format(REGX_HASH, account_hash.split("-")[2]):
        raise ValueError(
            "account-hash value should be 64 length only containing alphabet and number")


def check_clkey_bid_addr_format(bid_addr):
    # check format of hash
    inner_value = bid_addr.removeprefix("bid-addr-")
    bid_addr_tag = inner_value[0:2]
    hash_hex = inner_value[2:]
    print("bid_addr_tag: ", bid_addr_tag)

    match bid_addr_tag:
        case BID_ADDR_TAG.UnifiedTag:
            if not check_format(REGX_HASH, hash_hex):
                raise ValueError(
                    "hash value should be 64 length only containing alphabet and number")

        case BID_ADDR_TAG.ValidatorTag:
            if not check_format(REGX_HASH, hash_hex):
                raise ValueError(
                    "validator hash value should be 64 length only containing alphabet and number")

        case BID_ADDR_TAG.DelegatedAccountTag:
            validator_hash_hex = hash_hex[0:64]
            if not check_format(REGX_HASH, validator_hash_hex):
                raise ValueError(
                    "validator hash value should be 64 length only containing alphabet and number")
            delegator_hash_hex = hash_hex[64:]
            if not check_format(REGX_HASH, delegator_hash_hex):
                raise ValueError(
                    "delegator hash value should be 64 length only containing alphabet and number")

        case BID_ADDR_TAG.DelegatedPurseTag:
            validator_hash_hex = hash_hex[0:64]
            if not check_format(REGX_HASH, validator_hash_hex):
                raise ValueError(
                    "validator hash value should be 64 length only containing alphabet and number")
            delegator_purse_hex = hash_hex[64:]
            if not check_format(REGX_HASH, delegator_purse_hex):
                raise ValueError(
                    "delegator purse hash value should be 64 length only containing alphabet and number")

        # case BID_ADDR_TAG.CreditTag:
        #     pass
        case BID_ADDR_TAG.ReservedDelegationAccountTag:
            validator_hash_hex = hash_hex[0:64]
            if not check_format(REGX_HASH, validator_hash_hex):
                raise ValueError(
                    "validator hash value should be 64 length only containing alphabet and number")
            delegator_hash_hex = hash_hex[64:]
            if not check_format(REGX_HASH, delegator_hash_hex):
                raise ValueError(
                    "delegator hash value should be 64 length only containing alphabet and number")

        case BID_ADDR_TAG.ReservedDelegationPurseTag:
            validator_hash_hex = hash_hex[0:64]
            if not check_format(REGX_HASH, validator_hash_hex):
                raise ValueError(
                    "validator hash value should be 64 length only containing alphabet and number")
            delegator_purse_hex = hash_hex[64:]
            if not check_format(REGX_HASH, delegator_purse_hex):
                raise ValueError(
                    "delegator purse hash value should be 64 length only containing alphabet and number")

        case BID_ADDR_TAG.UnbondAccountTag:
            validator_hash_hex = hash_hex[0:64]
            if not check_format(REGX_HASH, validator_hash_hex):
                raise ValueError(
                    "validator hash value should be 64 length only containing alphabet and number")
            delegator_hash_hex = hash_hex[64:]
            if not check_format(REGX_HASH, delegator_hash_hex):
                raise ValueError(
                    "delegator hash value should be 64 length only containing alphabet and number")

        case BID_ADDR_TAG.UnbondPurseTag:
            validator_purse_hex = hash_hex[0:64]
            if not check_format(REGX_HASH, validator_purse_hex):
                raise ValueError(
                    "validator purse hash value should be 64 length only containing alphabet and number")
        case _:
            raise ValueError("not valid bid-addr prefix")


def check_clkey_hash_format(hash_value):
    if not check_format(REGX_HASH, hash_value):
        raise ValueError(
            "hash value should be 64 length only containing alphabet and number")


def check_block_format(block_id):
    if isinstance(block_id, str):
        if not check_format(REGX_HASH, block_id):
            raise ValueError(
                "block-hash value should be 64 length only containing alphabet and number")


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

    # key:bid-addr-xxx
    # elif clkey.startswith("bid-addr-"):
    #     check_bid_addr_format(clkey)
    # todo


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


def check_public_key_format(public_key):
    if not check_format(REGX_PUBLICKEY, public_key):
        raise ValueError(
            "publickey should be 01xxx(64 length) or 02xxx(66 length)")


def check_purse_format(purse):
    if not purse.startswith("uref-"):
        raise ValueError("purse should start with 'uref-'")
    if not purse.endswith(('000', '001', '002', '003', '004', '005', '006', '007')):
        raise ValueError("uref should end with '000 - 007'")
    if not check_format(REGX_HASH, purse.split("-")[1]):
        raise ValueError(
            "uref value should be 64 length only containing alphabet and number")


def check_root_state_hash_format(state_root_hash):
    if state_root_hash is not None:
        if not isinstance(state_root_hash, str):
            raise TypeError("state_root_hash should be type str")
        if not check_format(REGX_HASH, state_root_hash):
            raise ValueError(
                "state_root_hash should be 64 length only containing alphabet and number")
