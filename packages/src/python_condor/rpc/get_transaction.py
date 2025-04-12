"""Get transaction RPC module.

This module provides functionality for retrieving transaction information from the Casper network
via the info_get_transaction RPC method.
"""

from typing import Dict, Any

import requests

from ..utils import check_deploy_hash_format
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetTransction:
    """Class for handling the info_get_transaction RPC call.

    This class allows retrieving transaction information from the Casper network
    using either a transaction hash or deploy hash.
    """

    def __init__(self, url: str, transaction_hash: str, transaction_flag: bool = True) -> None:
        """Initialize a GetTransction instance.

        Args:
            url: The RPC endpoint URL.
            transaction_hash: The transaction or deploy hash to retrieve information for.
            transaction_flag: If True, treat the hash as a transaction hash; if False, treat as a deploy hash.

        Raises:
            ValueError: If transaction_hash is not in a valid format.
        """
        # check transaction/deploy_hash format
        check_deploy_hash_format(transaction_hash)

        if transaction_flag:
            payload = {"Version1": transaction_hash}
        else:
            payload = {"Deploy": transaction_hash}

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.INFO_GET_TRANSACTION,
            "params": {
                "transaction_hash": {**payload}
            }
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to get transaction information.

        Returns:
            The JSON response from the RPC call containing the transaction information.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
