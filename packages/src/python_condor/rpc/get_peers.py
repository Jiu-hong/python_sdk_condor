"""Get peers RPC module.

This module provides functionality for retrieving peer information from the Casper network
via the info_get_peers RPC method.
"""

from typing import Dict, Any

import requests

from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetPeers:
    """Class for handling the info_get_peers RPC call.

    This class allows retrieving information about the peers connected to a Casper network node.
    """

    def __init__(self, url: str) -> None:
        """Initialize a GetPeers instance.

        Args:
            url: The RPC endpoint URL.
        """
        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.INFO_GET_PEERS
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to get peer information.

        Returns:
            The JSON response from the RPC call containing the peer information.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
