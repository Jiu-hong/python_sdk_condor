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
    def CHAIN_GET_BLOCK():
        return "chain_get_block"

    @constant
    def CHAIN_GET_BLOCK_TRANSFERS():
        return "chain_get_block_transfers"
