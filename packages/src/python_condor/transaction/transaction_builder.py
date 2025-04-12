"""
Transaction Builder module for creating Casper transactions.

This module provides a fluent builder interface for creating different types of transactions:
- Native transactions
- Contract call transactions
- Session call transactions

The builders support:
- Setting transaction parameters (initiator, chain, TTL, payment)
- Specifying runtime arguments
- Configuring transaction targets
- Setting entry points
- Building and serializing transactions
"""

from __future__ import annotations
from typing import Dict, Any, List, Tuple, Optional

from ..constants import EntryPointKind, InvocationKind, PricingModeKind, RuntimeKind, TargetKind
from ..keys import KeyAlgorithm
from .entity_alias_target import EntityAliasTarget
from .entity_target import EntityTarget
from .package_hash_target import PackageHashTarget
from .package_name_target import PackageNameTarget
from .pricing_mode import PricingMode
from .transaction_entry_point import TransactionEntryPoint
from .transaction_native_target import TransactionNativeTarget
from .transaction_scheduling import TransactionScheduling
from .transaction_session_target import TransactionSessionTarget
from .transaction_v1 import TransactionV1
from .transaction_v1_payload import TransactionV1Payload


# Constants for transaction configuration
INVOCATIONKIND = InvocationKind()
TARGETKIND = TargetKind()
RUNTIMEKIND = RuntimeKind()
PRICINGMODE = PricingModeKind()
ENTRYPOINT = EntryPointKind()


class TransactionBuilder:
    """
    Base class for building Casper transactions.

    This class provides the core functionality for creating transactions:
    - Setting transaction parameters
    - Configuring runtime arguments
    - Building and serializing transactions

    Attributes:
        signers_keypaths_algo (List[Tuple[str, KeyAlgorithm]]): List of signers with their key paths and algorithms
        vm (str): The virtual machine type
        initiator_addr (str): The address of the transaction initiator
        chain_name (str): The name of the target chain
        ttl (int): Time to live in minutes
        pricing_mode (PricingMode): The pricing mode for the transaction
        args (Dict[str, Any]): The runtime arguments
        target: The transaction target
        entry_point (TransactionEntryPoint): The entry point for execution
    """

    def __init__(self, signers_keypaths_algo: List[Tuple[str, KeyAlgorithm]]) -> TransactionBuilder:
        """
        Initialize a transaction builder.

        Args:
            signers_keypaths_algo (List[Tuple[str, KeyAlgorithm]]): List of signers with their key paths and algorithms
        """
        self.signers_keypaths_algo = signers_keypaths_algo
        self.vm = RUNTIMEKIND.VMCASPERV1

    def from_publickey(self, public_key: str) -> TransactionBuilder:
        """
        Set the initiator's public key.

        Args:
            public_key (str): The initiator's public key

        Returns:
            TransactionBuilder: This builder instance
        """
        self.initiator_addr = public_key
        return self

    def chainname(self, name: str) -> TransactionBuilder:
        """
        Set the target chain name.

        Args:
            name (str): The chain name

        Returns:
            TransactionBuilder: This builder instance
        """
        self.chain_name = name
        return self

    def set_ttl(self, ttl: int) -> TransactionBuilder:
        """
        Set the transaction time to live.

        Args:
            ttl (int): Time to live in minutes

        Returns:
            TransactionBuilder: This builder instance
        """
        self.ttl = ttl
        return self

    def payment(self, payment_amount: int) -> TransactionBuilder:
        """
        Set the payment amount for the transaction.

        Args:
            payment_amount (int): The payment amount in motes

        Returns:
            TransactionBuilder: This builder instance
        """
        self.pricing_mode = PricingMode(PRICINGMODE.CLASSIC, payment_amount)
        return self

    def runtime_args(self, args: Dict[str, Any]) -> TransactionBuilder:
        """
        Set the runtime arguments for the transaction.

        Args:
            args (Dict[str, Any]): The runtime arguments

        Returns:
            TransactionBuilder: This builder instance
        """
        self.args = args
        return self

    def build(self) -> Dict[str, Any]:
        """
        Build and serialize the transaction.

        Returns:
            Dict[str, Any]: The JSON representation of the transaction
        """
        self.scheduling = TransactionScheduling()

        payload = TransactionV1Payload(
            self.args,
            self.target,
            self.entry_point,
            self.scheduling,
            self.initiator_addr,
            self.pricing_mode,
            self.chain_name
        )

        transaction = TransactionV1(payload, self.signers_keypaths_algo)
        return transaction.to_json()


class NativeBuilder(TransactionBuilder):
    """
    Builder for native transactions.

    Native transactions are used for system-level operations.
    """

    def __init__(self, data: List[Tuple[str, KeyAlgorithm]]):
        """
        Initialize a native transaction builder.

        Args:
            data (List[Tuple[str, KeyAlgorithm]]): List of signers with their key paths and algorithms
        """
        self.target = TransactionNativeTarget()
        super().__init__(data)

    def entry_point(self, name: str) -> NativeBuilder:
        """
        Set the entry point for the native transaction.

        Args:
            name (str): The entry point name

        Returns:
            NativeBuilder: This builder instance
        """
        self.entry_point = TransactionEntryPoint(name)
        return self


class ContractCallBuilder(TransactionBuilder):
    """
    Builder for contract call transactions.

    Contract calls can target:
    - Contracts by hash
    - Contracts by name
    - Packages by hash
    - Packages by name
    """

    def by_contract_hash(self, contract_hash: str) -> ContractCallBuilder:
        """
        Target a contract by its hash.

        Args:
            contract_hash (str): The contract hash

        Returns:
            ContractCallBuilder: This builder instance
        """
        target = EntityTarget(self.vm, contract_hash)
        self.target = target
        return self

    def by_contract_name(self, contract_name: str) -> ContractCallBuilder:
        """
        Target a contract by its name.

        Args:
            contract_name (str): The contract name

        Returns:
            ContractCallBuilder: This builder instance
        """
        target = EntityAliasTarget(self.vm, contract_name)
        self.target = target
        return self

    def by_package_hash(self, package_hash: str, version: Optional[int] = None) -> ContractCallBuilder:
        """
        Target a package by its hash.

        Args:
            package_hash (str): The package hash
            version (Optional[int], optional): The package version. Defaults to None.

        Returns:
            ContractCallBuilder: This builder instance
        """
        target = PackageHashTarget(self.vm, package_hash, version)
        self.target = target
        return self

    def by_package_name(self, package_name: str, version: Optional[int] = None) -> ContractCallBuilder:
        """
        Target a package by its name.

        Args:
            package_name (str): The package name
            version (Optional[int], optional): The package version. Defaults to None.

        Returns:
            ContractCallBuilder: This builder instance
        """
        target = PackageNameTarget(self.vm, package_name, version)
        self.target = target
        return self

    def entry_point(self, name: str) -> ContractCallBuilder:
        """
        Set the entry point for the contract call.

        Args:
            name (str): The entry point name

        Returns:
            ContractCallBuilder: This builder instance
        """
        self.entry_point = TransactionEntryPoint(ENTRYPOINT.CUSTOM, name)
        return self


class SessionCallBuilder(TransactionBuilder):
    """
    Builder for session call transactions.

    Session calls are used for deploying or upgrading contracts.
    """

    def __init__(self, data: List[Tuple[str, KeyAlgorithm]]):
        """
        Initialize a session call builder.

        Args:
            data (List[Tuple[str, KeyAlgorithm]]): List of signers with their key paths and algorithms
        """
        self.entry_point = TransactionEntryPoint(ENTRYPOINT.CALL)
        super().__init__(data)

    def module_bytes(self, module_bytes: str, is_install_upgrade: bool = False) -> SessionCallBuilder:
        """
        Set the module bytes for the session call.

        Args:
            module_bytes (str): The module bytes
            is_install_upgrade (bool, optional): Whether this is an install/upgrade call. Defaults to False.

        Returns:
            SessionCallBuilder: This builder instance
        """
        target = TransactionSessionTarget(
            self.vm, module_bytes, is_install_upgrade)
        self.target = target
        return self
