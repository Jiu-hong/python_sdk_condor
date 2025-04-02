import re

from ..constants import JsonName
from .deploy_name_arg import DeployNamedArg
from ..utils import serialize_string

JSONNAME = JsonName()


class SessionPackageHash:
    def __init__(self, package_hash, version, entrypoint, runtime_args):
        # check package_hash
        regx = "([0-9a-z]{64})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(package_hash)
        if not isinstance(result, re.Match):
            raise ValueError(
                "package-hash should only contain alphabet and number(64 length)")
        # check entrypoint
        if entrypoint == "":
            raise ValueError("The entrypoint shouldn't be empty.")
        self.package_hash = package_hash
        self.version = version
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        # tag
        StoredPackageByHashTag = int(3).to_bytes()

        # version
        if self.version is None:
            version_bytes = int(0).to_bytes()
        else:
            version_bytes = int(1).to_bytes() + \
                self.version.to_bytes(4, byteorder='little')

        result = StoredPackageByHashTag + bytes.fromhex(self.package_hash) + \
            version_bytes + \
            serialize_string(self.entrypoint) + \
            self.runtime_args.serialize()

        return result

    def to_json(self):
        result = {JSONNAME.SESSION: {
            JSONNAME.STOREDVERSIONEDCONTRACTBYHASH: {
                JSONNAME.HASH: self.package_hash,
                JSONNAME.VERSION: self.version,
                JSONNAME.ENTRYPOINT: self.entrypoint,
                JSONNAME.ARGS: self.runtime_args.to_json()
            }
        }}
        return result
