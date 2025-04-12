"""Query global state by state root hash RPC module.

This module provides functionality for querying the global state of the Casper network
via the query_global_state RPC method using a state root hash.
"""

from typing import Dict, Any, Optional

import requests

from ...utils import check_clkey_format, check_root_state_hash_format
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryGlobalState:
    """Class for handling the query_global_state RPC call using a state root hash.

    This class allows querying the global state of the Casper network
    for a specific key and optional state root hash.
    """

    def __init__(self, url: str, key: str, state_root_hash: Optional[str] = None) -> None:
        """Initialize a QueryGlobalState instance.

        Args:
            url: The RPC endpoint URL.
            key: The CL key to query.
            state_root_hash: Optional state root hash to query against.

        Raises:
            ValueError: If key is not in a valid format.
            ValueError: If state_root_hash is provided but not in a valid format.
        """
        # check key format
        check_clkey_format(key)

        # check state root hash format
        check_root_state_hash_format(state_root_hash)

        if state_root_hash is None:
            params = {
                "key": key
            }
        else:
            params = {
                "key": key,
                "state_identifier": {
                    "StateRootHash": state_root_hash
                }
            }

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_GLOBAL_STATE,
            "params": params
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to query the global state.

        Returns:
            The JSON response from the RPC call containing the global state information.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
