from ..constants import JsonName
from .deploy_name_arg import DeployNamedArg
from ..utils import serialize_string

JSONNAME = JsonName()


class SessionContractName:
    def __init__(self, contract_name,  entrypoint, runtime_args):
        if contract_name == "":
            raise ValueError("The contract name shouldn't be empty.")
        if entrypoint == "":
            raise ValueError("The entrypoint shouldn't be empty.")
        self.contract_name = contract_name
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        # tag StoredContractByNameTag = '02'
        StoredContractByNameTag = int(2).to_bytes()

        result = StoredContractByNameTag + serialize_string(self.contract_name) + \
            serialize_string(self.entrypoint) + \
            self.runtime_args.serialize()

        return result

    def to_json(self):
        result = {JSONNAME.SESSION: {
            JSONNAME.STOREDCONTRACTBYNAME: {
                JSONNAME.NAME: self.contract_name,
                JSONNAME.ENTRYPOINT: self.entrypoint,
                JSONNAME.ARGS: self.runtime_args.to_json()
            }
        }}
        return result
