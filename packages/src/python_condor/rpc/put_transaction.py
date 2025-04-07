import requests
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class PutTransction:
    def __init__(self, url, transactionV1: dict):
        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.ACCOUNT_PUT_TRANSACTION,
            "params": transactionV1}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        if x.status_code == requests.codes.ok:
            return x.json()
