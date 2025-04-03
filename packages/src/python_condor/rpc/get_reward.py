
import requests
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetReward:
    def __init__(self, url, validator, delegator: str = None, era: int = None):
        if validator is None:
            raise ValueError("validator is required.")

        if era is None:
            params = {
                "validator": validator,
                "delegator": delegator
            }
        else:
            params = {
                "validator": validator,
                "delegator": delegator,
                "era_identifier": {
                    "Era": era
                }
            }

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.INFO_GET_REWARD,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
