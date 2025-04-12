"""Put deploy RPC module.

This module provides functionality for submitting a deploy to the Casper network
via the account_put_deploy RPC method.
"""

from typing import Dict, Any

import requests

from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class PutDeploy:
    """Class for handling the account_put_deploy RPC call.

    This class allows submitting a deploy to the Casper network.
    """

    def __init__(self, url: str, deploy: Dict[str, Any]) -> None:
        """Initialize a PutDeploy instance.

        Args:
            url: The RPC endpoint URL.
            deploy: The deploy data to submit.
        """
        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.ACCOUNT_PUT_DEPLOY,
            "params": deploy
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to submit the deploy.

        Returns:
            The JSON response from the RPC call containing the deploy result.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
