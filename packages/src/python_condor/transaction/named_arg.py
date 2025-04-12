"""
Named Argument module for handling Casper named arguments.

This module provides functionality for managing named arguments in transactions.
Named arguments are used for:
- Passing parameters to contracts
- Specifying runtime arguments
- Managing CL value serialization

The module supports:
- Argument name and value management
- CL value serialization
- JSON representation
"""

from typing import Dict, Any, Tuple, Union

from ..utils import serialize_string


class NamedArg:
    """
    Represents a named argument in a Casper transaction.

    A named argument pairs a name with a CL value, allowing for structured
    parameter passing in transactions.

    Attributes:
        name (str): The name of the argument
        value (Any): The CL value of the argument
    """

    def __init__(self, name: str, value: Any):
        """
        Initialize a named argument.

        Args:
            name (str): The name of the argument
            value (Any): The CL value of the argument
        """
        self.name = name
        self.value = value  # CLValue

    def to_byte_with_named_arg(self) -> bytes:
        """
        Serialize the named argument to bytes.

        The serialization includes:
        - Argument name as a string
        - CL value data

        Returns:
            bytes: The serialized named argument
        """
        name_bytes = serialize_string(self.name)
        value_bytes = bytes.fromhex(self.value.cl_value())

        return name_bytes + value_bytes

    def to_json(self) -> Tuple[str, Dict[str, Any]]:
        """
        Convert the named argument to a JSON representation.

        The JSON structure follows the format:
        (name, {
            "cl_type": <cl_type_json>,
            "bytes": "<serialized_bytes>",
            "parsed": <parsed_value>
        })

        Returns:
            Tuple[str, Dict[str, Any]]: The JSON representation of the named argument
        """
        my_dict = {}
        my_dict["cl_type"] = self.value.to_json()
        my_dict["bytes"] = self.value.serialize().hex()
        my_dict["parsed"] = self.value.value()

        return self.name, my_dict
