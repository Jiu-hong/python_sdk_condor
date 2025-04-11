"""Get auction info v2 RPC module.

This module provides functionality for retrieving auction information from the Casper network
via the state_get_auction_info_v2 RPC method.
"""

from typing import Dict, Any, Optional, Union

import requests

from ..utils import check_block_format
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetAuctionInfoV2:
    """Class for handling the state_get_auction_info_v2 RPC call.

    This class allows retrieving auction information from the Casper network
    for a specific block height or hash.
    """

    def __init__(self, url: str, block_id: Optional[Union[int, str]] = None) -> None:
        """Initialize a GetAuctionInfoV2 instance.

        Args:
            url: The RPC endpoint URL.
            block_id: Optional block identifier (height or hash).

        Raises:
            ValueError: If block_id is not a valid height or hash.
        """
        # check block id format
        check_block_format(block_id)

        if block_id is None:
            params = {}
        elif isinstance(block_id, int):
            params = {
                "block_identifier": {
                    "Height": block_id
                }
            }
        elif isinstance(block_id, str):
            params = {
                "block_identifier": {
                    "Hash": block_id
                }
            }
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.STATE_GET_AUCTION_INFO_V2,
            "params": params
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to get auction info.

        Returns:
            The JSON response from the RPC call.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
