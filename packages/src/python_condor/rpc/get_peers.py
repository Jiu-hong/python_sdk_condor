
import requests
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetPeers:
    def __init__(self, url):
        self.url = url

        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.INFO_GET_PEERS}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
