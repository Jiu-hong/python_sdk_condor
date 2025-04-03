import requests

from ....utils import check_account_hash_format, check_root_state_hash_format
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalanceMainPurseAccountHash:
    def __init__(self, url, account_hash: str, state_root_hash: str = None):
        # check account_hash format
        check_account_hash_format(account_hash)
        # check state root hash format
        check_root_state_hash_format(state_root_hash)

        if state_root_hash is None:
            params = {
                "purse_identifier": {
                    "main_purse_under_account_hash": account_hash
                }}
        else:
            params = [
                {
                    "StateRootHash": state_root_hash
                },
                {
                    "main_purse_under_account_hash": account_hash
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
