from constants.base import constant


class JsonName(object):
    @constant
    def APPROVALS():
        return "approvals"

    @constant
    def CHAIN_NAME():
        return "chain_name"

    @constant
    def ENTRYPOINT():
        return "entry_point"

    @constant
    def HASH():
        return "hash"

    @constant
    def ID():
        return "id"

    @constant
    def IS_INSTALL_UPGRADE():
        return "is_install_upgrade"

    @constant
    def MODULEBYTES():
        return "module_bytes"

    @constant
    def NATIVE():
        return "Native"

    @constant
    def PAYLOAD():
        return "payload"

    @constant
    def RUNTIME():
        return "runtime"

    @constant
    def SCHEDULING():
        return "scheduling"

    @constant
    def SESSION():
        return "Session"

    @constant
    def SIGNATURE():
        return "signature"

    @constant
    def SIGNER():
        return "signer"

    @constant
    def STORED():
        return "Stored"

    @constant
    def TARGET():
        return "target"

    @constant
    def TIMESTAMP():
        return "timestamp"

    @constant
    def TRANSACTION():
        return "transaction"

    @constant
    def TTL():
        return "ttl"

    @constant
    def VERSION1():
        return "Version1"
