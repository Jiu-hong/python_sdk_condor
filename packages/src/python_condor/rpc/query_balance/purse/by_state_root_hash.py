import requests
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalancePurseUref:
    def __init__(self, url, purse_uref: str, state_root_hash: str = None):
        self.url = url
        if state_root_hash is None:
            params = {
                "purse_identifier": {
                    "purse_uref": purse_uref
                }}
        else:
            params = [
                {
                    "StateRootHash": state_root_hash
                },
                {
                    "purse_uref": purse_uref
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
