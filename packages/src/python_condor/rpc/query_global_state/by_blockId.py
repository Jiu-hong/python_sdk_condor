import requests

from ...utils import check_block_format, check_clkey_format
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryGlobalStateByBlockId:
    def __init__(self, url, key: str, block_id: int | str = None):
        # check key format
        check_clkey_format(key)
        # check state root hash format
        check_block_format(block_id)

        # construct params
        if block_id is None:
            params = {
                "key": key
            }

        elif isinstance(block_id, int):
            params = {
                "key": key,
                "state_identifier": {
                    "BlockHeight": block_id
                }
            }
        elif isinstance(block_id, str):
            params = {
                "key": key,
                "state_identifier": {
                    "BlockHash": block_id
                }
            }
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_GLOBAL_STATE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
