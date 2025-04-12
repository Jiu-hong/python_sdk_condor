"""Query balance by account hash and state root hash RPC module.

This module provides functionality for querying the balance of a main purse
via the query_balance RPC method using an account hash and state root hash.
"""

from typing import Dict, Any, Optional

import requests

from ....utils import check_account_hash_format, check_root_state_hash_format
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalanceMainPurseAccountHash:
    """Class for handling the query_balance RPC call using an account hash and state root hash.

    This class allows querying the balance of a main purse in the Casper network
    for a specific account hash and optional state root hash.
    """

    def __init__(self, url: str, account_hash: str, state_root_hash: Optional[str] = None) -> None:
        """Initialize a QueryBalanceMainPurseAccountHash instance.

        Args:
            url: The RPC endpoint URL.
            account_hash: The account hash to query the balance for.
            state_root_hash: Optional state root hash to query against.

        Raises:
            ValueError: If account_hash is not in a valid format.
            ValueError: If state_root_hash is provided but not in a valid format.
        """
        # check account_hash format
        check_account_hash_format(account_hash)
        # check state root hash format
        check_root_state_hash_format(state_root_hash)

        if state_root_hash is None:
            params = {
                "purse_identifier": {
                    "main_purse_under_account_hash": account_hash
                }
            }
        else:
            params = [
                {
                    "StateRootHash": state_root_hash
                },
                {
                    "main_purse_under_account_hash": account_hash
                }
            ]

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_BALANCE,
            "params": params
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to query the balance.

        Returns:
            The JSON response from the RPC call containing the balance information.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
