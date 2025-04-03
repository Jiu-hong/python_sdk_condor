import requests
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryGlobalState:
    def __init__(self, url, key: str, state_root_hash: None):
        self.url = url
        # construct params
        if state_root_hash is None:
            params = {
                "key": key
            }
        else:
            params = {
                "key": key,
                "state_identifier": {
                    "StateRootHash": state_root_hash
                }
            }
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_GLOBAL_STATE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
