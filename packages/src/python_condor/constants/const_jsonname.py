"""JSON name constants module.

This module provides constants for JSON field names used in the Casper network.
These constants are used for serialization and deserialization of JSON data.
"""

from .base import constant


class JsonName:
    """Class containing JSON field name constants.

    This class provides string names used for different JSON fields
    in the Casper network, such as deploy fields, contract fields,
    and transaction fields.
    """

    @constant
    def AMOUNT() -> str:
        """Get the amount field name."""
        return "amount"

    @constant
    def STOREDVERSIONEDCONTRACTBYHASH() -> str:
        """Get the stored versioned contract by hash field name."""
        return "StoredVersionedContractByHash"

    @constant
    def STOREDCONTRACTBYHASH() -> str:
        """Get the stored contract by hash field name."""
        return "StoredContractByHash"

    @constant
    def STOREDCONTRACTBYNAME() -> str:
        """Get the stored contract by name field name."""
        return "StoredContractByName"

    @constant
    def STOREDVERSIONEDCONTRACTBYNAME() -> str:
        """Get the stored versioned contract by name field name."""
        return "StoredVersionedContractByName"

    @constant
    def MILLISECONDS() -> str:
        """Get the milliseconds field name."""
        return "milliseconds"

    @constant
    def PARSED() -> str:
        """Get the parsed field name."""
        return "parsed"

    @constant
    def BYTES() -> str:
        """Get the bytes field name."""
        return "bytes"

    @constant
    def CL_TYPE() -> str:
        """Get the CL type field name."""
        return "cl_type"

    @constant
    def DEPLOY() -> str:
        """Get the deploy field name."""
        return "deploy"

    @constant
    def HEADER() -> str:
        """Get the header field name."""
        return "header"

    @constant
    def ACCOUNT() -> str:
        """Get the account field name."""
        return "account"

    @constant
    def APPROVALS() -> str:
        """Get the approvals field name."""
        return "approvals"

    @constant
    def CHAIN_NAME() -> str:
        """Get the chain name field name."""
        return "chain_name"

    @constant
    def ENTRYPOINT() -> str:
        """Get the entry point field name."""
        return "entry_point"

    @constant
    def HASH() -> str:
        """Get the hash field name."""
        return "hash"

    @constant
    def ID() -> str:
        """Get the ID field name."""
        return "id"

    @constant
    def IS_INSTALL_UPGRADE() -> str:
        """Get the is install upgrade field name."""
        return "is_install_upgrade"

    @constant
    def MODULE_BYTES() -> str:
        """Get the module bytes field name."""
        return "module_bytes"

    @constant
    def MODULEBYTES() -> str:
        """Get the ModuleBytes field name."""
        return "ModuleBytes"

    @constant
    def NATIVE() -> str:
        """Get the native field name."""
        return "Native"

    @constant
    def PAYLOAD() -> str:
        """Get the payload field name."""
        return "payload"

    @constant
    def RUNTIME() -> str:
        """Get the runtime field name."""
        return "runtime"

    @constant
    def SCHEDULING() -> str:
        """Get the scheduling field name."""
        return "scheduling"

    @constant
    def TRANSACTION_SESSION() -> str:
        """Get the transaction session field name."""
        return "Session"

    @constant
    def DEPLOY_SESSION() -> str:
        """Get the deploy session field name."""
        return "session"

    @constant
    def SIGNATURE() -> str:
        """Get the signature field name."""
        return "signature"

    @constant
    def SIGNER() -> str:
        """Get the signer field name."""
        return "signer"

    @constant
    def STORED() -> str:
        """Get the stored field name."""
        return "Stored"

    @constant
    def TARGET() -> str:
        """Get the target field name."""
        return "target"

    @constant
    def TIMESTAMP() -> str:
        """Get the timestamp field name."""
        return "timestamp"

    @constant
    def TRANSACTION() -> str:
        """Get the transaction field name."""
        return "transaction"

    @constant
    def TTL() -> str:
        """Get the TTL field name."""
        return "ttl"

    @constant
    def VERSION1() -> str:
        """Get the Version1 field name."""
        return "Version1"

    @constant
    def BYPACKAGENAME() -> str:
        """Get the by package name field name."""
        return "ByPackageName"

    @constant
    def NAME() -> str:
        """Get the name field name."""
        return "name"

    @constant
    def VERSION() -> str:
        """Get the version field name."""
        return "version"

    @constant
    def BYPACKAGEHASH() -> str:
        """Get the by package hash field name."""
        return "ByPackageHash"

    @constant
    def ADDR() -> str:
        """Get the address field name."""
        return "addr"

    @constant
    def PAYMENT() -> str:
        """Get the payment field name."""
        return "payment"

    @constant
    def FIELDS() -> str:
        """Get the fields field name."""
        return "fields"

    @constant
    def ARGS() -> str:
        """Get the args field name."""
        return "args"

    @constant
    def NAMED() -> str:
        """Get the named field name."""
        return "Named"

    @constant
    def PAYMENTLIMITED() -> str:
        """Get the payment limited field name."""
        return "PaymentLimited"

    @constant
    def PAYMENT_AMOUNT() -> str:
        """Get the payment amount field name."""
        return "payment_amount"

    @constant
    def GAS_PRICE() -> str:
        """Get the gas price field name."""
        return "gas_price"

    @constant
    def BODY_HASH() -> str:
        """Get the body hash field name."""
        return "body_hash"

    @constant
    def DEPENDENCIES() -> str:
        """Get the dependencies field name."""
        return "dependencies"

    @constant
    def GAS_PRICE_TOLERACE() -> str:
        """Get the gas price tolerance field name."""
        return "gas_price_tolerance"

    @constant
    def STANDARD_PAYMENT() -> str:
        """Get the standard payment field name."""
        return "standard_payment"

    @constant
    def PRICING_MODE() -> str:
        """Get the pricing mode field name."""
        return "pricing_mode"

    @constant
    def BYHASH() -> str:
        """Get the by hash field name."""
        return "ByHash"

    @constant
    def BYNAME() -> str:
        """Get the by name field name."""
        return "ByName"
