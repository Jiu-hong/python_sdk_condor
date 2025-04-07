import requests
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class PutDeploy:
    def __init__(self, url, deploy: dict):
        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.ACCOUNT_PUT_DEPLOY,
            "params": deploy}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        if x.status_code == requests.codes.ok:
            return x.json()
