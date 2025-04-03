import requests

from python_condor.utils import check_deploy_hash_format
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetDeploy:
    def __init__(self, url, deploy_hash: str = None):
        # check deploy_hash format
        check_deploy_hash_format(deploy_hash)

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.INFO_GET_DEPLOY,
            "params": {
                "deploy_hash": deploy_hash
            }}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
