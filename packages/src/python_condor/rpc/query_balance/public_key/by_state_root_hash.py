import requests
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalanceMainPursePublicKey:
    def __init__(self, url, main_purse_under_public_key: str, state_root_hash: str = None):
        self.url = url
        if state_root_hash is None:
            params = {
                "purse_identifier": {
                    "main_purse_under_public_key": main_purse_under_public_key
                }}
        else:
            params = [
                {
                    "StateRootHash": state_root_hash
                },
                {
                    "main_purse_under_public_key": "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
                }
            ]
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_BALANCE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
