import re

from ..constants import JsonName
from .deploy_name_arg import DeployNamedArg
from ..utils import serialize_string


JSONNAME = JsonName()


class SessionContractHash:
    def __init__(self, contract_hash, entrypoint, runtime_args):
        # check contract_hash
        regx = "([0-9a-z]{64})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(contract_hash)
        if not isinstance(result, re.Match):
            raise ValueError(
                "contract-hash should only contain alphabet and number(64 length)")
        # check entrypoint
        if entrypoint == "":
            raise ValueError("The entrypoint shouldn't be empty.")
        self.contract_hash = contract_hash
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        # tag StoredContractByHashTag = '01'
        StoredContractByHashTag = int(1).to_bytes()

        result = StoredContractByHashTag + bytes.fromhex(self.contract_hash) + \
            serialize_string(self.entrypoint) + \
            self.runtime_args.serialize()

        return result

    def to_json(self):
        result = {JSONNAME.DEPLOY_SESSION: {
            JSONNAME.STOREDCONTRACTBYHASH: {
                JSONNAME.HASH: self.contract_hash,
                JSONNAME.ENTRYPOINT: self.entrypoint,
                JSONNAME.ARGS: self.runtime_args.to_json()
            }
        }}
        return result
