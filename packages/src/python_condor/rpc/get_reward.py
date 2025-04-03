
import requests

from ..utils import check_public_key_format
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetReward:
    def __init__(self, url, validator: str, delegator: str = None, era: int = None):

        if validator is None:
            raise ValueError("validator is required.")

        # check validator format
        check_public_key_format(validator)

        if delegator is not None:
            # check delegator format
            check_public_key_format(delegator)

        if era is not None and not isinstance(era, int):
            raise TypeError("era should be int")

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
