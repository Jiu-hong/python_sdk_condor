from __future__ import annotations

from .deploy import Deploy
from .deploy_header import DeployHeader
from .session_payment import SessionPayment
from .session_contract_hash import SessionContractHash
from .session_contract_name import SessionContractName
from .session_package_name import SessionPackageName
from .session_package_hash import SessionPackageHash
from .session_module_bytes import SessionModuleBytes


class DeployBuilder:
    def __init__(self, signers_keypaths_algo) -> DeployBuilder:
        self.signers_keypaths_algo = signers_keypaths_algo

    def from_publickey(self, account: str) -> DeployBuilder:
        self.account = account
        return self

    def chainname(self, name) -> DeployBuilder:
        self.chain_name = name
        return self

    def set_ttl(self, ttl: int) -> DeployBuilder:
        self.ttl = ttl
        return self

    def payment(self, payment_amount) -> DeployBuilder:
        self.payment = SessionPayment(payment_amount)
        return self


class SessionContractHashBuilder(DeployBuilder):
    def by_contract_hash(self, contract_hash) -> SessionContractHashBuilder:
        self.contract_hash = contract_hash
        return self

    def entry_point(self, entry_point) -> SessionContractHashBuilder:
        self.entry_point = entry_point
        return self

    def runtime_args(self, args) -> SessionContractHashBuilder:
        self.args = args
        return self

    def build(self) -> dict:
        session = SessionContractHash(
            self.contract_hash, self.entry_point, self.args)
        header = DeployHeader(self.account, self.chain_name)
        deploy = Deploy(header, self.payment, session,
                        self.signers_keypaths_algo)
        return deploy.to_json()


class SessionContractNameBuilder(DeployBuilder):
    def by_contract_name(self, contract_name) -> SessionContractNameBuilder:
        self.contract_name = contract_name
        return self

    def entry_point(self, entry_point) -> SessionContractNameBuilder:
        self.entry_point = entry_point
        return self

    def runtime_args(self, args) -> SessionContractNameBuilder:
        self.args = args
        return self

    def build(self) -> dict:
        session = SessionContractName(
            self.contract_name, self.entry_point, self.args)
        header = DeployHeader(self.account, self.chain_name)
        deploy = Deploy(header, self.payment, session,
                        self.signers_keypaths_algo)
        return deploy.to_json()


class SessionPackageNameBuilder(DeployBuilder):
    def by_package_name(self, package_name, version=None) -> SessionPackageNameBuilder:
        self.package_name = package_name
        self.version = version
        return self

    def entry_point(self, entry_point) -> SessionPackageNameBuilder:
        self.entry_point = entry_point
        return self

    def runtime_args(self, args) -> SessionPackageNameBuilder:
        self.args = args
        return self

    def build(self) -> dict:
        session = SessionPackageName(
            self.package_name, self.version, self.entry_point, self.args)
        header = DeployHeader(self.account, self.chain_name)
        deploy = Deploy(header, self.payment, session,
                        self.signers_keypaths_algo)
        return deploy.to_json()


class SessionPackageHashBuilder(DeployBuilder):
    def by_package_hash(self, package_hash, version=None) -> SessionPackageHashBuilder:
        self.package_hash = package_hash
        self.version = version
        return self

    def entry_point(self, entry_point) -> SessionPackageHashBuilder:
        self.entry_point = entry_point
        return self

    def runtime_args(self, args) -> SessionPackageHashBuilder:
        self.args = args
        return self

    def build(self) -> dict:
        session = SessionPackageHash(
            self.package_hash, self.version, self.entry_point, self.args)
        header = DeployHeader(self.account, self.chain_name)
        deploy = Deploy(header, self.payment, session,
                        self.signers_keypaths_algo)
        return deploy.to_json()


class SessionModuleBytesBuilder(DeployBuilder):
    def module_bytes(self, module_bytes, version=None) -> SessionModuleBytesBuilder:
        self.module_bytes = module_bytes
        self.version = version
        return self

    def runtime_args(self, args) -> SessionModuleBytesBuilder:
        self.args = args
        return self

    def build(self) -> dict:
        session = SessionModuleBytes(
            self.module_bytes, self.args)
        header = DeployHeader(self.account, self.chain_name)
        deploy = Deploy(header, self.payment, session,
                        self.signers_keypaths_algo)
        return deploy.to_json()
