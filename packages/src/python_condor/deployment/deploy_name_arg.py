"""Deploy named arguments module.

This module provides functionality for handling named arguments in Casper network deployments.
"""

from typing import Dict, List, Tuple

from ..constants import JsonName
from ..utils import serialize_string


JSONNAME = JsonName()


class DeployNamedArg:
    """Class for managing named arguments in deployments.

    This class handles the serialization and JSON conversion of named arguments
    used in Casper network deployments.
    """

    def __init__(self, args: Dict[str, object]):
        """Initialize named arguments.

        Args:
            args: Dictionary of named arguments where values should be CLValue objects.

        Raises:
            ValueError: If any argument value is not a CLValue object.
        """
        for arg_value in args.values():
            if not hasattr(arg_value, "tag"):
                raise ValueError("The value for NamedArg should be CLValue.")
        self.args = args

    def serialize(self) -> bytes:
        """Serialize the named arguments to bytes.

        Returns:
            Bytes representation of the named arguments.
        """
        inner_serialize = b''
        for name, value in self.args.items():
            s_name = serialize_string(name)
            inner_serialize += s_name
            s_value = bytes.fromhex(value.cl_value())
            inner_serialize += s_value

        list_length = int(len(self.args)).to_bytes(4, "little")
        return list_length + inner_serialize

    def to_json(self) -> List[Tuple[str, Dict]]:
        """Convert named arguments to JSON format.

        Returns:
            List of tuples containing argument names and their JSON representations.
        """
        args_list = []
        for key, value in self.args.items():
            my_dict = {
                JSONNAME.CL_TYPE: value.to_json(),
                JSONNAME.BYTES: value.serialize().hex(),
                JSONNAME.PARSED: value.value()
            }
            args_list.append((key, my_dict))
        return args_list
