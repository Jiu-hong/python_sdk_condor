import requests

from python_condor.utils import REGX_PUBLICKEY, check_format, REGX_HASH, check_public_key_format, check_root_state_hash_format
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalanceMainPursePublicKey:
    def __init__(self, url, public_key: str, state_root_hash: str = None):
        # check publickey format
        check_public_key_format(public_key)
        # check state root hash format
        check_root_state_hash_format(state_root_hash)

        if state_root_hash is None:
            params = {
                "purse_identifier": {
                    "main_purse_under_public_key": public_key
                }}
        else:
            params = [
                {
                    "StateRootHash": state_root_hash
                },
                {
                    "main_purse_under_public_key": public_key
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
