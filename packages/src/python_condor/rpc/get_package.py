import requests
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetPackage:
    def __init__(self, url, ContractPackageHash, block_id: int | str = None):
        self.url = url
        if block_id is None:
            params = {}
        elif isinstance(block_id, int):
            params = [
                {
                    "ContractPackageHash": ContractPackageHash
                },
                {
                    "Height": block_id
                }
            ]
        elif isinstance(block_id, str):
            params = [
                {
                    "ContractPackageHash": ContractPackageHash
                },
                {
                    "Hash": block_id
                }
            ]
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")

        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.STATE_GET_PACKAGE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
