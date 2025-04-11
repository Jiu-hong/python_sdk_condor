"""Get package RPC module.

This module provides functionality for retrieving contract package information from the Casper network
via the state_get_package RPC method.
"""

from typing import Dict, Any, Optional, Union, List

import requests

from ..utils import check_block_format, check_contract_package_format
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetPackage:
    """Class for handling the state_get_package RPC call.

    This class allows retrieving contract package information from the Casper network
    for a specific contract package hash and optional block height or hash.
    """

    def __init__(self, url: str, contract_package: str, block_id: Optional[Union[int, str]] = None) -> None:
        """Initialize a GetPackage instance.

        Args:
            url: The RPC endpoint URL.
            contract_package: The contract package hash to retrieve information for.
            block_id: Optional block identifier (height or hash).

        Raises:
            ValueError: If contract_package is not in a valid format or block_id is not a valid height or hash.
        """
        # check contract_package format
        check_contract_package_format(contract_package)
        # check block id format
        check_block_format(block_id)

        if block_id is None:
            params = {
                "package_identifier": {
                    "ContractPackageHash": contract_package
                }
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
            "params": params
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to get package information.

        Returns:
            The JSON response from the RPC call containing the package information.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
