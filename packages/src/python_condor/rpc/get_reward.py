"""Get reward RPC module.

This module provides functionality for retrieving reward information from the Casper network
via the info_get_reward RPC method.
"""

from typing import Dict, Any, Optional

import requests

from ..utils import check_public_key_format
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class GetReward:
    """Class for handling the info_get_reward RPC call.

    This class allows retrieving reward information for validators and delegators
    in the Casper network.
    """

    def __init__(self, url: str, validator: str, delegator: Optional[str] = None, era: Optional[int] = None) -> None:
        """Initialize a GetReward instance.

        Args:
            url: The RPC endpoint URL.
            validator: The public key of the validator to get rewards for.
            delegator: Optional public key of the delegator to get rewards for.
            era: Optional era number to get rewards for.

        Raises:
            ValueError: If validator is not provided or not in a valid format.
            ValueError: If delegator is provided but not in a valid format.
            TypeError: If era is provided but not an integer.
        """
        if validator is None:
            raise ValueError("validator is required.")

        # check validator format
        check_public_key_format(validator)

        if delegator is not None:
            # check delegator format
            check_public_key_format(delegator)

        if era is not None and not isinstance(era, int):
            raise TypeError("era should be int")

        if era is None:
            params = {
                "validator": validator,
                "delegator": delegator
            }
        else:
            params = {
                "validator": validator,
                "delegator": delegator,
                "era_identifier": {
                    "Era": era
                }
            }

        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.INFO_GET_REWARD,
            "params": params
        }

    def run(self) -> Dict[str, Any]:
        """Send the RPC request to get reward information.

        Returns:
            The JSON response from the RPC call containing the reward information.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
