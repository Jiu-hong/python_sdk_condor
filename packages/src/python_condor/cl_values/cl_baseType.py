"""CL base type module.

This module provides base classes for CL (Casper) value types used in the Casper network.
These base classes define the common interface for all CL value types.
"""

from typing import Any, Dict, Union

from ..utils import get_deep_value, get_deep_json, get_cl_tags


class CLValue:
    """Base class for all CL value types.

    This class provides the common interface for all CL value types,
    including serialization, JSON conversion, and value retrieval.
    """

    def __init__(self, data: Any) -> None:
        """Initialize a CL value.

        Args:
            data: The underlying data for this CL value.
        """
        self.data = data

    def value(self) -> Any:
        """Get the underlying value of this CL value.

        Returns:
            The underlying value of this CL value.
        """
        return get_deep_value(self)

    def cl_value(self) -> str:
        """Convert this CL value to its hexadecimal string representation.

        The representation includes:
        - Length of the serialized content (4 bytes, little-endian)
        - Serialized content
        - Type tag

        Returns:
            Hexadecimal string representation of this CL value.
        """
        content = self.serialize()
        bytes_len = int(len(content)).to_bytes(4, byteorder='little')

        tag = get_cl_tags(self)
        return (bytes_len + content + tag).hex()

    def to_json(self) -> Dict[str, Any]:
        """Convert this CL value to its JSON representation.

        Returns:
            Dictionary containing the JSON representation of this CL value.
        """
        return get_deep_json(self)
