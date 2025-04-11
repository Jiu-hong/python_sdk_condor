"""Deploy header module.

This module provides functionality for managing deployment headers in Casper network deployments.
"""

import re
from datetime import datetime, timezone
from hashlib import blake2b
from typing import Dict

from ..cl_values import CLPublicKey
from ..constants import JsonName
from ..utils import serialize_string


JSONNAME = JsonName()


class DeployHeader:
    """Class for managing deployment headers.

    This class handles the creation and management of headers for Casper network deployments,
    including account information, chain name, timestamps, and other metadata.
    """

    def __init__(
        self,
        account: str,
        chain_name: str,
        now: datetime = datetime.now(timezone.utc),
        ttl: int = 30,
        gas_price: int = 1
    ):
        """Initialize a deployment header.

        Args:
            account: The account public key (01xxx or 02xxx format).
            chain_name: The name of the chain.
            now: The current timestamp (defaults to current UTC time).
            ttl: Time to live in minutes (defaults to 30).
            gas_price: Gas price for the deployment (defaults to 1).

        Raises:
            ValueError: If account format is invalid or chain_name is empty.
            TypeError: If now, ttl, or gas_price are of incorrect types.
        """
        # Check account pattern
        regx = "(01[0-9a-zA-Z]{64})|(02[0-9a-zA-Z]{66})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(account)
        if not isinstance(result, re.Match):
            raise ValueError(
                "account should be 01xxx(64 length) or 02xxx(66 length)"
            )

        # Check chain-name
        if chain_name == "":
            raise ValueError("The chain_name shouldn't be empty.")

        # Check time
        if not isinstance(now, datetime):
            raise TypeError("time should be type datetime.datetime")

        # Check ttl
        if not isinstance(ttl, int):
            raise TypeError("ttl should be type int")

        # Check gas_price
        if not isinstance(gas_price, int):
            raise TypeError("gas_price should be type int")

        self.account = account
        self.chain_name = chain_name
        self.time = now
        self.ttl = ttl
        self.gas_price = gas_price

    def add_body_hash(self, body_hash: str) -> None:
        """Add the body hash to the header.

        Args:
            body_hash: The hash of the deployment body.
        """
        self.body_hash = body_hash

    def to_bytes(self) -> bytes:
        """Convert the header to bytes.

        Returns:
            Bytes representation of the header.
        """
        s_account = CLPublicKey(self.account).serialize()
        s_time_now = int(self.time.timestamp() *
                         1000).to_bytes(8, byteorder='little')
        s_ttl = (int(self.ttl) * 60000).to_bytes(8, byteorder='little')
        s_gas_price = self.gas_price.to_bytes(8, byteorder='little')
        s_body_hash = bytes.fromhex(self.body_hash)
        s_dependencies = bytes.fromhex("00000000")
        s_chain_name = serialize_string(self.chain_name)

        return (
            s_account + s_time_now + s_ttl + s_gas_price +
            s_body_hash + s_dependencies + s_chain_name
        )

    def byteHash(self) -> str:
        """Calculate the hash of the header.

        Returns:
            The hex digest of the header hash.
        """
        header_bytes = self.to_bytes()
        h = blake2b(digest_size=32)
        h.update(header_bytes)
        return h.hexdigest()

    def to_json(self) -> Dict:
        """Convert the header to JSON format.

        Returns:
            Dictionary containing the header in JSON format.
        """
        return {
            JSONNAME.HEADER: {
                JSONNAME.ACCOUNT: self.account,
                JSONNAME.TIMESTAMP: self.time.replace(
                    tzinfo=None
                ).isoformat(timespec=JSONNAME.MILLISECONDS) + "Z",
                JSONNAME.TTL: str(self.ttl) + 'm',
                JSONNAME.GAS_PRICE: self.gas_price,
                JSONNAME.BODY_HASH: self.body_hash,
                JSONNAME.DEPENDENCIES: [],
                JSONNAME.CHAIN_NAME: self.chain_name
            }
        }
