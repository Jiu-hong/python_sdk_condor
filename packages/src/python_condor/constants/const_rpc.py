"""RPC method constants module.

This module provides constants for RPC (Remote Procedure Call) method names
used in the Casper network node communication.
"""

from .base import constant


class RpcMethod:
    """Class containing RPC method name constants.

    This class provides string names used for different RPC methods
    in the Casper network node communication.
    """

    @constant
    def ACCOUNT_PUT_DEPLOY() -> str:
        """Get the account put deploy RPC method name."""
        return "account_put_deploy"

    @constant
    def ACCOUNT_PUT_TRANSACTION() -> str:
        """Get the account put transaction RPC method name."""
        return "account_put_transaction"

    @constant
    def CHAIN_GET_BLOCK() -> str:
        """Get the chain get block RPC method name."""
        return "chain_get_block"

    @constant
    def CHAIN_GET_BLOCK_TRANSFERS() -> str:
        """Get the chain get block transfers RPC method name."""
        return "chain_get_block_transfers"

    @constant
    def INFO_GET_DEPLOY() -> str:
        """Get the info get deploy RPC method name."""
        return "info_get_deploy"

    @constant
    def CHAIN_GET_ERA_SUMMARY() -> str:
        """Get the chain get era summary RPC method name."""
        return "chain_get_era_summary"

    @constant
    def CHAIN_GET_STATE_ROOT_HASH() -> str:
        """Get the chain get state root hash RPC method name."""
        return "chain_get_state_root_hash"

    @constant
    def INFO_GET_PEERS() -> str:
        """Get the info get peers RPC method name."""
        return "info_get_peers"

    @constant
    def INFO_GET_REWARD() -> str:
        """Get the info get reward RPC method name."""
        return "info_get_reward"

    @constant
    def INFO_GET_STATUS() -> str:
        """Get the info get status RPC method name."""
        return "info_get_status"

    @constant
    def INFO_GET_TRANSACTION() -> str:
        """Get the info get transaction RPC method name."""
        return "info_get_transaction"

    @constant
    def QUERY_BALANCE() -> str:
        """Get the query balance RPC method name."""
        return "query_balance"

    @constant
    def QUERY_GLOBAL_STATE() -> str:
        """Get the query global state RPC method name."""
        return "query_global_state"

    @constant
    def STATE_GET_ACCOUNT_INFO() -> str:
        """Get the state get account info RPC method name."""
        return "state_get_account_info"

    @constant
    def STATE_GET_AUCTION_INFO_V2() -> str:
        """Get the state get auction info v2 RPC method name."""
        return "state_get_auction_info_v2"

    @constant
    def STATE_GET_AUCTION_INFO() -> str:
        """Get the state get auction info RPC method name."""
        return "state_get_auction_info"

    @constant
    def STATE_GET_PACKAGE() -> str:
        """Get the state get package RPC method name."""
        return "state_get_package"
