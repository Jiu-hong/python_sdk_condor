from ..constants import JsonName
from .deploy_name_arg import DeployNamedArg
from ..utils import serialize_string

JSONNAME = JsonName()


class SessionPackageName:
    def __init__(self, package_name, version, entrypoint, runtime_args):
        if package_name == "":
            raise ValueError("The package name shouldn't be empty.")
        if entrypoint == "":
            raise ValueError("The entrypoint shouldn't be empty.")
        self.package_name = package_name
        self.version = version
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        # tag
        StoredPackageByNameTag = int(4).to_bytes()

        # version
        if self.version is None:
            version_bytes = int(0).to_bytes()
        else:
            version_bytes = int(1).to_bytes() + \
                self.version.to_bytes(4, byteorder='little')

        result = StoredPackageByNameTag + serialize_string(self.package_name) + \
            version_bytes + \
            serialize_string(self.entrypoint) + \
            self.runtime_args.serialize()

        return result

    def to_json(self):
        result = {JSONNAME.SESSION: {
            JSONNAME.STOREDVERSIONEDCONTRACTBYNAME: {
                JSONNAME.NAME: self.package_name,
                JSONNAME.VERSION: self.version,
                JSONNAME.ENTRYPOINT: self.entrypoint,
                JSONNAME.ARGS: self.runtime_args.to_json()
            }
        }}
        return result
