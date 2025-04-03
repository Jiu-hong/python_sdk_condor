import requests

from python_condor.utils import check_account_hash_format, check_block_format
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetAccountInfoByAccountHash:
    def __init__(self, url, account_hash: str, block_id: int | str = None):
        # check account hash format
        check_account_hash_format(account_hash)
        # check block id format
        check_block_format(block_id)

        if block_id is None:
            params = {
                "account_identifier": account_hash
            }
        elif isinstance(block_id, int):
            params = {
                "block_identifier": {
                    "Height": block_id
                },
                "account_identifier": account_hash
            }
        elif isinstance(block_id, str):
            params = {
                "block_identifier": {
                    "Hash": block_id
                },
                "account_identifier": account_hash
            }
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.STATE_GET_ACCOUNT_INFO,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
