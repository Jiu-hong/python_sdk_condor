from .base import constant


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

    @constant
    def BYPACKAGENAME():
        return "ByPackageName"

    @constant
    def NAME():
        return "name"

    @constant
    def VERSION():
        return "version"

    @constant
    def BYPACKAGEHASH():
        return "ByPackageHash"

    @constant
    def ADDR():
        return "addr"

    @constant
    def FIELDS():
        return "fields"

    @constant
    def ARGS():
        return "args"

    @constant
    def NAMED():
        return "Named"

    @constant
    def PAYMENTLIMITED():
        return "PaymentLimited"

    @constant
    def PAYMENT_AMOUNT():
        return "payment_amount"

    @constant
    def GAS_PRICE_TOLERACE():
        return "gas_price_tolerance"

    @constant
    def STANDARD_PAYMENT():
        return "standard_payment"

    @constant
    def PRICING_MODE():
        return "pricing_mode"

    @constant
    def BYHASH():
        return "ByHash"

    @constant
    def BYNAME():
        return "ByName"
