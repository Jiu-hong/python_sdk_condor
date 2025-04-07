import requests

from ..utils import check_block_format, check_contract_package_format
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetPackage:
    def __init__(self, url, contract_package: str, block_id: int | str = None):
        # check contract_package format
        check_contract_package_format(contract_package)
        # check block id format
        check_block_format(block_id)

        if block_id is None:
            params = {"package_identifier":
                      {"ContractPackageHash": contract_package}
                      }

        elif isinstance(block_id, int):
            params = [
                {
                    "ContractPackageHash": contract_package
                },
                {
                    "Height": block_id
                }
            ]
        elif isinstance(block_id, str):
            params = [
                {
                    "ContractPackageHash": contract_package
                },
                {
                    "Hash": block_id
                }
            ]
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.STATE_GET_PACKAGE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        if x.status_code == requests.codes.ok:
            return x.json()
