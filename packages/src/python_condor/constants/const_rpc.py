# Node RPC endpoints.
from .base import constant


class RpcMethod(object):
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
    def CHAIN_GET_BLOCK_TRANSFERS():
        return "chain_get_block_transfers"
