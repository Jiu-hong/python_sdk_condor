from python_condor.cl_values.cl_number import CLU512
from python_condor.constants.cons_jsonname import JsonName
from python_condor.deployment.deploy_name_arg import DeployNamedArg


JSONNAME = JsonName()


class SessionPayment:
    def __init__(self, payment_amount):
        self.payment_amount = DeployNamedArg(
            {JSONNAME.AMOUNT: CLU512(payment_amount)})

    def to_bytes(self) -> bytes:
        ModuleBytesTag = int(0).to_bytes()
        moduleBytes = bytes.fromhex("00000000")
        result = ModuleBytesTag + \
            moduleBytes + \
            self.payment_amount.serialize()
        return result

    def to_json(self):
        result = {JSONNAME.PAYMENT: {
            JSONNAME.MODULEBYTES: {
                JSONNAME.MODULE_BYTES: "",
                JSONNAME.ARGS: self.payment_amount.to_json()
            }
        }}
        return result
