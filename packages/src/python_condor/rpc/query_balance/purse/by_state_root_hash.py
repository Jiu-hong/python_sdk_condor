import requests

from ....utils import check_purse_format, check_root_state_hash_format
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalancePurseUref:
    def __init__(self, url, purse_uref: str, state_root_hash: str = None):
       # check purse format
        check_purse_format(purse_uref)
        # check state root hash format
        check_root_state_hash_format(state_root_hash)

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

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_BALANCE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
