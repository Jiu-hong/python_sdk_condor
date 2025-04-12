"""Query balance by account hash and block ID RPC module.

This module provides functionality for querying the balance of a main purse
via the query_balance RPC method using an account hash and block ID.
"""

from typing import Dict, Any, Optional, Union

import requests

from ....utils import check_account_hash_format, check_block_format
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalanceMainPurseAccountHashByBlockId:
    """Class for handling the query_balance RPC call using an account hash and block ID.

    This class allows querying the balance of a main purse in the Casper network
    for a specific account hash and optional block height or hash.
    """

    def __init__(self, url: str, account_hash: str, block_id: Optional[Union[int, str]] = None) -> None:
        """Initialize a QueryBalanceMainPurseAccountHashByBlockId instance.

        Args:
            url: The RPC endpoint URL.
            account_hash: The account hash to query the balance for.
            block_id: Optional block identifier (height or hash).

        Raises:
            ValueError: If account_hash is not in a valid format.
            ValueError: If block_id is not a valid height or hash.
        """
        # check account_hash format
        check_account_hash_format(account_hash)
        # check block_id format
        check_block_format(block_id)

        if block_id is None:
            params = {
                "purse_identifier": {
                    "main_purse_under_account_hash": account_hash
                }
            }
        elif isinstance(block_id, int):
            params = [
                {
                    "BlockHeight": block_id
                },
                {
                    "main_purse_under_account_hash": account_hash
                }
            ]
        elif isinstance(block_id, str):
            params = [
                {
                    "BlockHash": block_id
                },
                {
                    "main_purse_under_account_hash": account_hash
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
