"""Query balance by purse UREF and state root hash RPC module.

This module provides functionality for querying the balance of a purse
via the query_balance RPC method using a purse UREF and state root hash.
"""

from typing import Dict, Any, Optional

import requests

from ....utils import check_purse_format, check_root_state_hash_format
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalancePurseUref:
    """Class for handling the query_balance RPC call using a purse UREF and state root hash.

    This class allows querying the balance of a purse in the Casper network
    for a specific purse UREF and optional state root hash.
    """

    def __init__(self, url: str, purse_uref: str, state_root_hash: Optional[str] = None) -> None:
        """Initialize a QueryBalancePurseUref instance.

        Args:
            url: The RPC endpoint URL.
            purse_uref: The purse UREF to query the balance for.
            state_root_hash: Optional state root hash to query against.

        Raises:
            ValueError: If purse_uref is not in a valid format.
            ValueError: If state_root_hash is provided but not in a valid format.
        """
        # check purse format
        check_purse_format(purse_uref)
        # check state root hash format
        check_root_state_hash_format(state_root_hash)

        if state_root_hash is None:
            params = {
                "purse_identifier": {
                    "purse_uref": purse_uref
                }
            }
        else:
            params = [
                {
                    "StateRootHash": state_root_hash
                },
                {
                    "purse_uref": purse_uref
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
