import requests
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetTransction:
    def __init__(self, url, transaction_hash: str, transaction_flag: bool = True):
        self.url = url
        if transaction_flag:
            payload = {"Version1": transaction_hash}
        else:
            payload = {"Deploy": transaction_hash}
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.INFO_GET_TRANSACTION,
            "params": {
                "transaction_hash": {**payload}
            }}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
