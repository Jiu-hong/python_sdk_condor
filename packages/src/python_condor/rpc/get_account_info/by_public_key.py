import requests
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetAccountInfoByPublicKeyByBlockId:
    def __init__(self, url, public_key: str, block_id: int | str):
        self.url = url
        if isinstance(block_id, int):
            params = {
                "block_identifier": {
                    "Height": block_id
                },
                "public_key": public_key
            }
        elif isinstance(block_id, str):
            params = {
                "block_identifier": {
                    "Hash": block_id
                },
                "public_key": public_key
            }
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.STATE_GET_ACCOUNT_INFO,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
