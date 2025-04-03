import requests

from python_condor.utils import REGX_HASH, REGX_PUBLICKEY, check_block_format, check_format, check_public_key_format
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalanceMainPursePublicKeyByBlockId:
    def __init__(self, url, public_key: str, block_id: int | str = None):
        # check publickey format
        check_public_key_format(public_key)
        # check block_id format
        check_block_format(block_id)

        if block_id is None:
            params = {
                "purse_identifier": {
                    "main_purse_under_public_key": public_key
                }}
        elif isinstance(block_id, int):
            params = [
                {
                    "BlockHeight": block_id
                },
                {
                    "main_purse_under_public_key": public_key
                }
            ]
        elif isinstance(block_id, str):
            params = [
                {
                    "BlockHash": block_id
                },
                {
                    "main_purse_under_public_key": public_key
                }
            ]
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")
        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_BALANCE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
