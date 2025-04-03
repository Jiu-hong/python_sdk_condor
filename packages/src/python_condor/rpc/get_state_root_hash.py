import requests

from ..utils import check_block_format
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()

# chain_get_state_root_hash


class GetStateRootHash:
    def __init__(self, url, block_id: int | str = None):
        # check block id format
        check_block_format(block_id)

        if block_id is None:
            params = {}
        elif isinstance(block_id, int):
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

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.CHAIN_GET_STATE_ROOT_HASH,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
