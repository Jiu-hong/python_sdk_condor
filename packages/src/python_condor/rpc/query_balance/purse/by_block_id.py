"""Query balance by purse UREF and block ID RPC module.

This module provides functionality for querying the balance of a purse
via the query_balance RPC method using a purse UREF and block ID.
"""

from typing import Dict, Any, Optional, Union

import requests

from ....utils import check_block_format, check_purse_format
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalancePurseUrefByBlockId:
    """Class for handling the query_balance RPC call using a purse UREF and block ID.

    This class allows querying the balance of a purse in the Casper network
    for a specific purse UREF and optional block height or hash.
    """

    def __init__(self, url: str, purse_uref: str, block_id: Optional[Union[int, str]] = None) -> None:
        """Initialize a QueryBalancePurseUrefByBlockId instance.

        Args:
            url: The RPC endpoint URL.
            purse_uref: The purse UREF to query the balance for.
            block_id: Optional block identifier (height or hash).

        Raises:
            ValueError: If purse_uref is not in a valid format.
            ValueError: If block_id is not a valid height or hash.
        """
        # check purse format
        check_purse_format(purse_uref)
        # check block_id format
        check_block_format(block_id)

        if block_id is None:
            params = {
                "purse_identifier": {
                    "purse_uref": purse_uref
                }
            }
        elif isinstance(block_id, int):
            params = [
                {
                    "BlockHeight": block_id
                },
                {
                    "purse_uref": purse_uref
                }
            ]
        elif isinstance(block_id, str):
            params = [
                {
                    "BlockHash": block_id
                },
                {
                    "purse_uref": purse_uref
                }
            ]
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")

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
