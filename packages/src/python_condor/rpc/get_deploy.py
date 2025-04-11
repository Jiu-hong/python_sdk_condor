"""Get deploy RPC module.

This module provides functionality for retrieving deploy information from the Casper network
via the info_get_deploy RPC method.
"""

from typing import Dict, Any, Optional

import requests

from ..utils import check_deploy_hash_format
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetDeploy:
    """Class for handling the info_get_deploy RPC call.

    This class allows retrieving deploy information from the Casper network
    using a deploy hash.
    """

    def __init__(self, url: str, deploy_hash: Optional[str] = None) -> None:
        """Initialize a GetDeploy instance.

        Args:
            url: The RPC endpoint URL.
            deploy_hash: Optional deploy hash to retrieve information for.

        Raises:
            ValueError: If deploy_hash is not in a valid format.
        """
        # check deploy_hash format
        check_deploy_hash_format(deploy_hash)

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.INFO_GET_DEPLOY,
            "params": {
                "deploy_hash": deploy_hash
            }
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to get deploy information.

        Returns:
            The JSON response from the RPC call containing the deploy information.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
