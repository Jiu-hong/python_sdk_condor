from ..constants import JsonName
from .deploy_name_arg import DeployNamedArg


JSONNAME = JsonName()


class SessionModuleBytes:
    def __init__(self, module_bytes, runtime_args):
        self.module_bytes = bytes.fromhex(module_bytes)
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        ModuleBytesTag = int(0).to_bytes()

        module_bytes_length = len(
            self.module_bytes).to_bytes(4, byteorder='little')

        result = ModuleBytesTag + module_bytes_length +\
            self.module_bytes + \
            self.runtime_args.serialize()

        return result

    def to_json(self):
        result = {JSONNAME.DEPLOY_SESSION: {
            JSONNAME.MODULEBYTES: {
                JSONNAME.MODULE_BYTES: self.module_bytes.hex(),
                JSONNAME.ARGS: self.runtime_args.to_json()
            }
        }}
        return result
