from ..cl_values import CLU512
from ..constants import JsonName
from .deploy_name_arg import DeployNamedArg


JSONNAME = JsonName()


class SessionPayment:
    def __init__(self, payment_amount):
        self.payment_amount = DeployNamedArg(
            {JSONNAME.AMOUNT: CLU512(payment_amount)})

    def to_bytes(self) -> bytes:
        ModuleBytesTag = int(0).to_bytes()
        # length is 0
        module_bytes_length = int(0).to_bytes(4, byteorder='little')
        # module_bytes is null
        moduleBytes = b''
        result = ModuleBytesTag + module_bytes_length + \
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
