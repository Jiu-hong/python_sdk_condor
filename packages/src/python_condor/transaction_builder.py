from __future__ import annotations

from .constants import EntryPointKind, InvocationKind, PricingModeKind, RuntimeKind, TargetKind


from .pricing_mode import PricingMode
from .transaction_entry_point import TransactionEntryPoint
from .transaction_scheduling import TransactionScheduling
from .transaction_target import TransactionTarget
from .transaction_v1 import TransactionV1
from .transaction_v1_payload import TransactionV1Payload


INVOCATIONKIND = InvocationKind()
TARGETKIND = TargetKind()
RUNTIMEKIND = RuntimeKind()
PRICINGMODE = PricingModeKind()
ENTRYPOINT = EntryPointKind()


class TransactionBuilder:
    def __init__(self, signers_keypaths_algo) -> TransactionBuilder:
        self.signers_keypaths_algo = signers_keypaths_algo

    def from_publickey(self, public_key: str) -> TransactionBuilder:
        self.initiator_addr = public_key
        return self

    def chainname(self, name) -> TransactionBuilder:
        self.chain_name = name
        return self

    def set_ttl(self, ttl: int) -> TransactionBuilder:
        self.ttl = ttl
        return self

    def payment(self, payment_amount) -> TransactionBuilder:
        self.pricing_mode = PricingMode(PRICINGMODE.CLASSIC, payment_amount)
        return self

    def runtime_args(self, args) -> TransactionBuilder:
        self.args = args
        return self

    def build(self) -> dict:
        self.scheduling = TransactionScheduling()

        payload = TransactionV1Payload(self.args, self.target, self.entry_point,
                                       self.scheduling, self.initiator_addr, self.pricing_mode, self.chain_name)

        transaction = TransactionV1(
            payload, self.signers_keypaths_algo)
        return transaction.to_json()


class ContractCallBuilder(TransactionBuilder):

    def by_contract_hash(self, contract_hash: str) -> ContractCallBuilder:

        target = TransactionTarget(RUNTIMEKIND.VMCASPERV1, TARGETKIND.STORED, INVOCATIONKIND.INVOCABLEENTITY,
                                   contract_hash)
        self.target = target
        return self

    def by_contract_name(self, contract_name: str) -> ContractCallBuilder:
        target = TransactionTarget(RUNTIMEKIND.VMCASPERV1, TARGETKIND.STORED, INVOCATIONKIND.INVOCABLEENTITYALIAS,
                                   contract_name)
        self.target = target
        return self

    def by_package_hash(self, package_hash, version: int = None) -> ContractCallBuilder:
        target = TransactionTarget(RUNTIMEKIND.VMCASPERV1, TARGETKIND.STORED, INVOCATIONKIND.PACKAGE,
                                   package_hash, version)
        self.target = target
        return self

    def by_package_name(self, package_name: str, version: int = None) -> ContractCallBuilder:
        target = TransactionTarget(RUNTIMEKIND.VMCASPERV1, TARGETKIND.STORED, INVOCATIONKIND.PACKAGEALIAS,
                                   package_name)
        self.target = target
        return self

    def entry_point(self, name: str) -> ContractCallBuilder:
        self.entry_point = TransactionEntryPoint(ENTRYPOINT.CUSTOM, name)
        return self


class SessionCallBuilder(TransactionBuilder):
    #   private _transactionInvocationTarget: TransactionInvocationTarget;
    def module_bytes(self, module_bytes: str, is_install_upgrade: bool = False) -> SessionCallBuilder:
        target = TransactionTarget(
            RUNTIMEKIND.VMCASPERV1, TARGETKIND.SESSION, module_bytes, is_install_upgrade)
        self.target = target
        return self

    def entry_point(self) -> SessionCallBuilder:
        self.entry_point = TransactionEntryPoint(ENTRYPOINT.CALL)
        return self
