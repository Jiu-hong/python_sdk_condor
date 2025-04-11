"""Deploy builder module.

This module provides builder classes for creating different types of deployments
on the Casper network, including contract hash, contract name, package name,
package hash, and module bytes deployments.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple, Union

from ..keys import KeyAlgorithm

from .deploy import Deploy
from .deploy_header import DeployHeader
from .session_contract_hash import SessionContractHash
from .session_contract_name import SessionContractName
from .session_module_bytes import SessionModuleBytes
from .session_package_hash import SessionPackageHash
from .session_package_name import SessionPackageName
from .session_payment import SessionPayment


class DeployBuilder:
    """Base builder class for creating deployments.

    This class provides the common functionality for building different types
    of deployments on the Casper network.
    """

    def __init__(
        self,
        signers_keypaths_algo: List[Tuple[str, KeyAlgorithm]]
    ) -> DeployBuilder:
        """Initialize the deploy builder.

        Args:
            signers_keypaths_algo: List of tuples containing signer key paths
                and their corresponding algorithms.
        """
        self.signers_keypaths_algo = signers_keypaths_algo

    def from_publickey(self, account: str) -> DeployBuilder:
        """Set the account public key for the deployment.

        Args:
            account: The account public key.

        Returns:
            The builder instance for method chaining.
        """
        self.account = account
        return self

    def chainname(self, name: str) -> DeployBuilder:
        """Set the chain name for the deployment.

        Args:
            name: The name of the chain.

        Returns:
            The builder instance for method chaining.
        """
        self.chain_name = name
        return self

    def set_ttl(self, ttl: int) -> DeployBuilder:
        """Set the time-to-live for the deployment.

        Args:
            ttl: Time to live in minutes.

        Returns:
            The builder instance for method chaining.
        """
        self.ttl = ttl
        return self

    def payment(self, payment_amount: Any) -> DeployBuilder:
        """Set the payment amount for the deployment.

        Args:
            payment_amount: The payment amount.

        Returns:
            The builder instance for method chaining.
        """
        self.payment = SessionPayment(payment_amount)
        return self


class SessionContractHashBuilder(DeployBuilder):
    """Builder for contract hash deployments."""

    def by_contract_hash(self, contract_hash: str) -> SessionContractHashBuilder:
        """Set the contract hash for the deployment.

        Args:
            contract_hash: The hash of the contract.

        Returns:
            The builder instance for method chaining.
        """
        self.contract_hash = contract_hash
        return self

    def entry_point(self, entry_point: str) -> SessionContractHashBuilder:
        """Set the entry point for the contract.

        Args:
            entry_point: The name of the entry point function.

        Returns:
            The builder instance for method chaining.
        """
        self.entry_point = entry_point
        return self

    def runtime_args(self, args: Dict[str, Any]) -> SessionContractHashBuilder:
        """Set the runtime arguments for the contract.

        Args:
            args: Dictionary of runtime arguments.

        Returns:
            The builder instance for method chaining.
        """
        self.args = args
        return self

    def build(self) -> Dict[str, Any]:
        """Build the deployment.

        Returns:
            Dictionary containing the deployment in JSON format.
        """
        session = SessionContractHash(
            self.contract_hash,
            self.entry_point,
            self.args
        )
        header = DeployHeader(self.account, self.chain_name)
        deploy = Deploy(
            header,
            self.payment,
            session,
            self.signers_keypaths_algo
        )
        return deploy.to_json()


class SessionContractNameBuilder(DeployBuilder):
    """Builder for contract name deployments."""

    def by_contract_name(self, contract_name: str) -> SessionContractNameBuilder:
        """Set the contract name for the deployment.

        Args:
            contract_name: The name of the contract.

        Returns:
            The builder instance for method chaining.
        """
        self.contract_name = contract_name
        return self

    def entry_point(self, entry_point: str) -> SessionContractNameBuilder:
        """Set the entry point for the contract.

        Args:
            entry_point: The name of the entry point function.

        Returns:
            The builder instance for method chaining.
        """
        self.entry_point = entry_point
        return self

    def runtime_args(self, args: Dict[str, Any]) -> SessionContractNameBuilder:
        """Set the runtime arguments for the contract.

        Args:
            args: Dictionary of runtime arguments.

        Returns:
            The builder instance for method chaining.
        """
        self.args = args
        return self

    def build(self) -> Dict[str, Any]:
        """Build the deployment.

        Returns:
            Dictionary containing the deployment in JSON format.
        """
        session = SessionContractName(
            self.contract_name,
            self.entry_point,
            self.args
        )
        header = DeployHeader(self.account, self.chain_name)
        deploy = Deploy(
            header,
            self.payment,
            session,
            self.signers_keypaths_algo
        )
        return deploy.to_json()


class SessionPackageNameBuilder(DeployBuilder):
    """Builder for package name deployments."""

    def by_package_name(
        self,
        package_name: str,
        version: Optional[str] = None
    ) -> SessionPackageNameBuilder:
        """Set the package name and version for the deployment.

        Args:
            package_name: The name of the package.
            version: Optional version of the package.

        Returns:
            The builder instance for method chaining.
        """
        self.package_name = package_name
        self.version = version
        return self

    def entry_point(self, entry_point: str) -> SessionPackageNameBuilder:
        """Set the entry point for the package.

        Args:
            entry_point: The name of the entry point function.

        Returns:
            The builder instance for method chaining.
        """
        self.entry_point = entry_point
        return self

    def runtime_args(self, args: Dict[str, Any]) -> SessionPackageNameBuilder:
        """Set the runtime arguments for the package.

        Args:
            args: Dictionary of runtime arguments.

        Returns:
            The builder instance for method chaining.
        """
        self.args = args
        return self

    def build(self) -> Dict[str, Any]:
        """Build the deployment.

        Returns:
            Dictionary containing the deployment in JSON format.
        """
        session = SessionPackageName(
            self.package_name,
            self.version,
            self.entry_point,
            self.args
        )
        header = DeployHeader(self.account, self.chain_name)
        deploy = Deploy(
            header,
            self.payment,
            session,
            self.signers_keypaths_algo
        )
        return deploy.to_json()


class SessionPackageHashBuilder(DeployBuilder):
    """Builder for package hash deployments."""

    def by_package_hash(
        self,
        package_hash: str,
        version: Optional[str] = None
    ) -> SessionPackageHashBuilder:
        """Set the package hash and version for the deployment.

        Args:
            package_hash: The hash of the package.
            version: Optional version of the package.

        Returns:
            The builder instance for method chaining.
        """
        self.package_hash = package_hash
        self.version = version
        return self

    def entry_point(self, entry_point: str) -> SessionPackageHashBuilder:
        """Set the entry point for the package.

        Args:
            entry_point: The name of the entry point function.

        Returns:
            The builder instance for method chaining.
        """
        self.entry_point = entry_point
        return self

    def runtime_args(self, args: Dict[str, Any]) -> SessionPackageHashBuilder:
        """Set the runtime arguments for the package.

        Args:
            args: Dictionary of runtime arguments.

        Returns:
            The builder instance for method chaining.
        """
        self.args = args
        return self

    def build(self) -> Dict[str, Any]:
        """Build the deployment.

        Returns:
            Dictionary containing the deployment in JSON format.
        """
        session = SessionPackageHash(
            self.package_hash,
            self.version,
            self.entry_point,
            self.args
        )
        header = DeployHeader(self.account, self.chain_name)
        deploy = Deploy(
            header,
            self.payment,
            session,
            self.signers_keypaths_algo
        )
        return deploy.to_json()


class SessionModuleBytesBuilder(DeployBuilder):
    """Builder for module bytes deployments."""

    def module_bytes(
        self,
        module_bytes: bytes,
        version: Optional[str] = None
    ) -> SessionModuleBytesBuilder:
        """Set the module bytes and version for the deployment.

        Args:
            module_bytes: The bytes of the module.
            version: Optional version of the module.

        Returns:
            The builder instance for method chaining.
        """
        self.module_bytes = module_bytes
        self.version = version
        return self

    def runtime_args(self, args: Dict[str, Any]) -> SessionModuleBytesBuilder:
        """Set the runtime arguments for the module.

        Args:
            args: Dictionary of runtime arguments.

        Returns:
            The builder instance for method chaining.
        """
        self.args = args
        return self

    def build(self) -> Dict[str, Any]:
        """Build the deployment.

        Returns:
            Dictionary containing the deployment in JSON format.
        """
        session = SessionModuleBytes(
            self.module_bytes,
            self.args
        )
        header = DeployHeader(self.account, self.chain_name)
        deploy = Deploy(
            header,
            self.payment,
            session,
            self.signers_keypaths_algo
        )
        return deploy.to_json()
