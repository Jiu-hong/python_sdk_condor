"""Query global state by block ID RPC module.

This module provides functionality for querying the global state of the Casper network
via the query_global_state RPC method using a block height or hash.
"""

from typing import Dict, Any, Optional, Union

import requests

from ...utils import check_block_format, check_clkey_format
from ...constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryGlobalStateByBlockId:
    """Class for handling the query_global_state RPC call using a block ID.

    This class allows querying the global state of the Casper network
    for a specific key and optional block height or hash.
    """

    def __init__(self, url: str, key: str, block_id: Optional[Union[int, str]] = None) -> None:
        """Initialize a QueryGlobalStateByBlockId instance.

        Args:
            url: The RPC endpoint URL.
            key: The CL key to query.
            block_id: Optional block identifier (height or hash).

        Raises:
            ValueError: If key is not in a valid format.
            ValueError: If block_id is not a valid height or hash.
        """
        # check key format
        check_clkey_format(key)
        # check state root hash format
        check_block_format(block_id)

        # construct params
        if block_id is None:
            params = {
                "key": key
            }
        elif isinstance(block_id, int):
            params = {
                "key": key,
                "state_identifier": {
                    "BlockHeight": block_id
                }
            }
        elif isinstance(block_id, str):
            params = {
                "key": key,
                "state_identifier": {
                    "BlockHash": block_id
                }
            }
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")

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
