# Node RPC endpoints.
from .base import constant


class RpcMethod(object):
    @constant
    def STATE_GET_AUCTION_INFO():
        return "state_get_auction_info"

    @constant
    def STATE_GET_ACCOUNT_INFO():
        return "state_get_account_info"

    @constant
    def QUERY_BALANCE():
        return "query_balance"

    @constant
    def INFO_GET_PEERS():
        return "info_get_peers"

    @constant
    def INFO_GET_STATUS():
        return "info_get_status"

    @constant
    def QUERY_GLOBAL_STATE():
        return "query_global_state"

    @constant
    def ACCOUNT_PUT_TRANSACTION():
        return "account_put_transaction"

    @constant
    def ACCOUNT_PUT_DEPLOY():
        return "account_put_deploy"

    @constant
    def INFO_GET_TRANSACTION():
        return "info_get_transaction"

    @constant
    def INFO_GET_DEPLOY():
        return "info_get_deploy"

    @constant
    def CHAIN_GET_BLOCK():
        return "chain_get_block"

    @constant
    def CHAIN_GET_STATE_ROOT_HASH():
        return "chain_get_state_root_hash"

    @constant
    def CHAIN_GET_BLOCK_TRANSFERS():
        return "chain_get_block_transfers"
