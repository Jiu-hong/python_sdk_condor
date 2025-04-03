import requests
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryGlobalState:
    def __init__(self, url, key: str):
        self.url = url
        # construct params
        params = {
            "key": key
        }
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_GLOBAL_STATE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
