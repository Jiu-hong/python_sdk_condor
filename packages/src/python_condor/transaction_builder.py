from __future__ import annotations

from python_condor.constants.cons_target import TargetKind
from python_condor.constants.const_runtime import RuntimeKind
from python_condor.pricing_mode import PricingMode
from python_condor.transaction_entry_point import TransactionEntryPoint
from python_condor.transaction_scheduling import TransactionScheduling
from python_condor.transaction_target import TransactionTarget
from .transaction_invocation_target import TransactionInvocationTarget
from .transaction_v1_payload import TransactionV1Payload
from .transaction_v1 import TransactionV1
from .constants import InvocationKind

# payload = TransactionV1Payload(self.initiatorAddr, self.timestamp, self.ttl, self.chain_name,  self.pricing_mode, self.args, self.target,
#                                self.entrypoint, self.scheduling)
# transaction = TransactionV1(
#     payload, self.signers_keypaths_algo)


INVOCATIONKIND = InvocationKind()
TARGETKIND = TargetKind()
RUNTIMEKIND = RuntimeKind()
# print("CONST:", CONST)


class TransactionBuilder:
    def __init__(self, signers_keypaths_algo):
        self.signers_keypaths_algo = signers_keypaths_algo

    def from_publickey(self, public_key: str):
        self.initiator_addr = public_key
        return self

    def chainname(self, name):
        self.chain_name = name
        return self

    def set_ttl(self, ttl: int):
        self.ttl = ttl
        return self

    def payment(self, payment_amount):
        self.pricing_mode = PricingMode("Classic", payment_amount)
        return self

    def args(self, args):
        self.args = args
        return self

    def build(self) -> dict:
        self.scheduling = TransactionScheduling()

        payload = TransactionV1Payload(self.args, self.target, self.entry_point,
                                       self.scheduling, self.initiator_addr, self.pricing_mode, self.chain_name)
        # payload = TransactionV1Payload(args, target1,
        #                        entrypoint1, scheduling, initiatorAddr, pricing_mode, chain_name)
        transaction = TransactionV1(
            payload, self.signers_keypaths_algo)
        return transaction.to_json()


class ContractCallBuilder(TransactionBuilder):
    #   private _transactionInvocationTarget: TransactionInvocationTarget;
    def by_contract_hash(self, contract_hash: str) -> ContractCallBuilder:
        # invocation_target = TransactionInvocationTarget(
        #     CONST.INVOCABLEENTITY, contract_hash)
        target = TransactionTarget(RUNTIMEKIND.VMCASPERV1, TARGETKIND.STORED, INVOCATIONKIND.INVOCABLEENTITY,
                                   contract_hash)
        self.target = target
        return self

    def by_contract_name(self, contract_name):
        target = TransactionTarget(RUNTIMEKIND.VMCASPERV1, TARGETKIND.STORED, INVOCATIONKIND.INVOCABLEENTITYALIAS,
                                   contract_name)
        self.target = target
        return self
        #   public byName(name: string): ContractCallBuilder {
        #     const invocationTarget = new TransactionInvocationTarget();
        #     invocationTarget.byName = name;
        #     this._transactionInvocationTarget = invocationTarget;

        #     const storedTarget = new StoredTarget();
        #     storedTarget.id = invocationTarget;
        #     storedTarget.runtime = TransactionRuntime.vmCasperV1();

        #     this._invocationTarget = new TransactionTarget(undefined, storedTarget);
        #     return this;
        #   }

    def by_package_hash(self, package_hash, version: int = None):
        target = TransactionTarget(RUNTIMEKIND.VMCASPERV1, TARGETKIND.STORED, INVOCATIONKIND.PACKAGE,
                                   package_hash, version)
        self.target = target
        return self
        #   public byPackageHash(
        #     contractHash: string,
        #     version?: number
        #   ): ContractCallBuilder {
        #     const packageHashInvocationTarget = new ByPackageHashInvocationTarget();
        #     packageHashInvocationTarget.addr = Hash.fromHex(contractHash);
        #     packageHashInvocationTarget.version = version;
        #     const transactionInvocationTarget = new TransactionInvocationTarget();
        #     transactionInvocationTarget.byPackageHash = packageHashInvocationTarget;
        #     this._transactionInvocationTarget = transactionInvocationTarget;

        #     const storedTarget = new StoredTarget();

        #     storedTarget.id = transactionInvocationTarget;
        #     storedTarget.runtime = TransactionRuntime.vmCasperV1();

        #     this._invocationTarget = new TransactionTarget(undefined, storedTarget);
        #     return this;
        #   }

    def by_package_name(self, package_name: str, version: int = None):
        target = TransactionTarget(RUNTIMEKIND.VMCASPERV1, TARGETKIND.STORED, INVOCATIONKIND.PACKAGEALIAS,
                                   package_name)
        self.target = target
        return self
        #   public byPackageName(name: string, version?: number): ContractCallBuilder {
        #     const packageNameInvocationTarget = new ByPackageNameInvocationTarget();
        #     packageNameInvocationTarget.name = name;
        #     packageNameInvocationTarget.version = version;
        #     const transactionInvocationTarget = new TransactionInvocationTarget();
        #     transactionInvocationTarget.byPackageName = packageNameInvocationTarget;
        #     this._transactionInvocationTarget = transactionInvocationTarget;

        #     const storedTarget = new StoredTarget();

        #     storedTarget.id = transactionInvocationTarget;
        #     storedTarget.runtime = TransactionRuntime.vmCasperV1();

        #     this._invocationTarget = new TransactionTarget(undefined, storedTarget);

        #     return this;
        #   }

    def entry_point(self, name: str):
        self.entry_point = TransactionEntryPoint("Custom", name)
        return self

    def runtime_args(self, args):
        self.args = args
        return self
