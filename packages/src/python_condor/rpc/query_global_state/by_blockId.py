import requests

from python_condor.utils import check_block_format, check_root_state_hash_format
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryGlobalStateByBlockId:
    def __init__(self, url, key: str, block_id: int | str):

        # check state root hash format
        check_block_format(block_id)

        self.url = url
        # construct params
        if isinstance(block_id, int):
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
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_GLOBAL_STATE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
