import requests

from python_condor.utils import check_clkey_format, check_root_state_hash_format
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryGlobalState:
    def __init__(self, url, key: str, state_root_hash: str = None):
        # check key format
        check_clkey_format(key)

        # check state root hash format
        check_root_state_hash_format(state_root_hash)

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

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_GLOBAL_STATE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
