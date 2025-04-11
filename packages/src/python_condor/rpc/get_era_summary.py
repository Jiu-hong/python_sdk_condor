"""Get era summary RPC module.

This module provides functionality for retrieving era summary information from the Casper network
via the chain_get_era_summary RPC method.
"""

from typing import Dict, Any, Optional, Union

import requests

from ..utils import check_block_format
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetEraSummary:
    """Class for handling the chain_get_era_summary RPC call.

    This class allows retrieving era summary information from the Casper network
    for a specific block height or hash.
    """

    def __init__(self, url: str, block_id: Optional[Union[int, str]] = None) -> None:
        """Initialize a GetEraSummary instance.

        Args:
            url: The RPC endpoint URL.
            block_id: Optional block identifier (height or hash).

        Raises:
            ValueError: If block_id is not a valid height or hash.
        """
        # check block id format
        check_block_format(block_id)

        if block_id is None:
            params = {}
        elif isinstance(block_id, int):
            params = {
                "block_identifier": {
                    "Height": block_id
                }
            }
        elif isinstance(block_id, str):
            params = {
                "block_identifier": {
                    "Hash": block_id
                }
            }
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.CHAIN_GET_ERA_SUMMARY,
            "params": params
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to get era summary information.

        Returns:
            The JSON response from the RPC call containing the era summary information.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
