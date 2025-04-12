"""Get account info by account hash RPC module.

This module provides functionality for retrieving account information from the Casper network
via the state_get_account_info RPC method using an account hash.
"""

from typing import Dict, Any, Optional, Union

import requests

from ...utils import check_account_hash_format, check_block_format
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetAccountInfoByAccountHash:
    """Class for handling the state_get_account_info RPC call using an account hash.

    This class allows retrieving account information from the Casper network
    for a specific account hash and optional block height or hash.
    """

    def __init__(self, url: str, account_hash: str, block_id: Optional[Union[int, str]] = None) -> None:
        """Initialize a GetAccountInfoByAccountHash instance.

        Args:
            url: The RPC endpoint URL.
            account_hash: The account hash to get account information for.
            block_id: Optional block identifier (height or hash).

        Raises:
            ValueError: If account_hash is not in a valid format.
            ValueError: If block_id is not a valid height or hash.
        """
        # check account hash format
        check_account_hash_format(account_hash)
        # check block id format
        check_block_format(block_id)

        if block_id is None:
            params = {
                "account_identifier": account_hash
            }
        elif isinstance(block_id, int):
            params = {
                "block_identifier": {
                    "Height": block_id
                },
                "account_identifier": account_hash
            }
        elif isinstance(block_id, str):
            params = {
                "block_identifier": {
                    "Hash": block_id
                },
                "account_identifier": account_hash
            }
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.STATE_GET_ACCOUNT_INFO,
            "params": params
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to get account information.

        Returns:
            The JSON response from the RPC call containing the account information.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
