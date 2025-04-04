import requests

from ....utils import check_block_format, check_purse_format
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalancePurseUrefByBlockId:
    def __init__(self, url, purse_uref: str, block_id: int | str = None):
        # check purse format
        check_purse_format(purse_uref)
        # check block_id format
        check_block_format(block_id)
        if block_id is None:
            params = {
                "purse_identifier": {
                    "purse_uref": purse_uref
                }}
        elif isinstance(block_id, int):
            params = [
                {
                    "BlockHeight": block_id
                },
                {
                    "purse_uref": purse_uref
                }
            ]
        elif isinstance(block_id, str):
            params = [
                {
                    "BlockHash": block_id
                },
                {
                    "purse_uref": purse_uref
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
