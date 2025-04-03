import requests

from python_condor.utils import check_block_format, check_public_key_format
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetAccountInfoByPublicKey:
    def __init__(self, url, public_key: str, block_id: int | str = None):
        # check public key format
        check_public_key_format(public_key)
        # check block id format
        check_block_format(block_id)

        if block_id is None:
            params = {
                "public_key": public_key
            }

        elif isinstance(block_id, int):
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

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.STATE_GET_ACCOUNT_INFO,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
