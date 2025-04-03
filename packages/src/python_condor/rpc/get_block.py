import requests
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetBlock:
    def __init__(self, url, block_id: int | str = None):
        self.url = url
        if block_id is None:
            params = {}
        if isinstance(block_id, int):
            params = {
                "block_identifier": {
                    "Height": block_id
                }
            }
        elif isinstance(block_id, str):
            params = {
                "block_identifier": {
                    "Hash": block_id
                }
            }
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")

        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.CHAIN_GET_BLOCK,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
