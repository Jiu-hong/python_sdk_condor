"""Query balance by public key and state root hash RPC module.

This module provides functionality for querying the balance of a main purse
via the query_balance RPC method using a public key and state root hash.
"""

from typing import Dict, Any, Optional, List, Union

import requests

from ....utils import check_public_key_format, check_root_state_hash_format
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalanceMainPursePublicKey:
    """Class for handling the query_balance RPC call using a public key and state root hash.

    This class allows querying the balance of a main purse in the Casper network
    for a specific public key and optional state root hash.
    """

    def __init__(self, url: str, public_key: str, state_root_hash: Optional[str] = None) -> None:
        """Initialize a QueryBalanceMainPursePublicKey instance.

        Args:
            url: The RPC endpoint URL.
            public_key: The public key to query the balance for.
            state_root_hash: Optional state root hash to query against.

        Raises:
            ValueError: If public_key is not in a valid format.
            ValueError: If state_root_hash is provided but not in a valid format.
        """
        # check publickey format
        check_public_key_format(public_key)
        # check state root hash format
        check_root_state_hash_format(state_root_hash)

        if state_root_hash is None:
            params = {
                "purse_identifier": {
                    "main_purse_under_public_key": public_key
                }
            }
        else:
            params = [
                {
                    "StateRootHash": state_root_hash
                },
                {
                    "main_purse_under_public_key": public_key
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
