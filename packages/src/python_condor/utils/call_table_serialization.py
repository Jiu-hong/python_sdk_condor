"""Call table serialization utilities.

This module provides functionality for serializing call tables in the Casper network,
allowing fields to be added in order and serialized to bytes.
"""

from typing import List, Tuple, Union


class CalltableSerialization:
    """Class for serializing call tables.

    This class manages a list of fields with their indices and offsets,
    and provides methods to add fields and serialize them to bytes.
    """

    def __init__(self) -> None:
        """Initialize a new CalltableSerialization instance.

        The instance starts with an empty list of fields and a current offset of 0.
        """
        self.fields: List[Tuple[int, int, bytes]] = []
        self.current_offset = 0

    def add_field(self, index: int, value: bytes) -> 'CalltableSerialization':
        """Add a field to the call table.

        Args:
            index: The index of the field.
            value: The bytes value of the field.

        Returns:
            The CalltableSerialization instance for method chaining.

        Raises:
            Exception: If fields are not added in the correct index order.
        """
        if len(self.fields) != index:
            raise Exception("Add fields in correct index order.")
        field = (index, self.current_offset, value)
        self.fields.append(field)
        self.current_offset += len(value)
        return self

    def to_bytes(self) -> bytes:
        """Serialize the call table to bytes.

        The format is:
        - 4 bytes: number of fields (little-endian)
        - For each field:
            - 2 bytes: field index (little-endian)
            - 4 bytes: field offset (little-endian)
        - 4 bytes: total payload size (little-endian)
        - All field values concatenated

        Returns:
            The serialized call table as bytes.
        """
        calltable_bytes = b''
        payload_bytes = b''

        calltable_bytes += len(self.fields).to_bytes(4, byteorder='little')

        for field in self.fields:
            calltable_bytes += field[0].to_bytes(2, byteorder='little')
            calltable_bytes += field[1].to_bytes(4, byteorder='little')
            payload_bytes += field[2]

        calltable_bytes += self.current_offset.to_bytes(4, byteorder='little')

        return calltable_bytes + payload_bytes
