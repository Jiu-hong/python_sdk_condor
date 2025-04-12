"""Get status RPC module.

This module provides functionality for retrieving node status information from the Casper network
via the info_get_status RPC method.
"""

from typing import Dict, Any

import requests

from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetStatus:
    """Class for handling the info_get_status RPC call.

    This class allows retrieving status information about a Casper network node.
    """

    def __init__(self, url: str) -> None:
        """Initialize a GetStatus instance.

        Args:
            url: The RPC endpoint URL.
        """
        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.INFO_GET_STATUS
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to get node status information.

        Returns:
            The JSON response from the RPC call containing the node status information.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
