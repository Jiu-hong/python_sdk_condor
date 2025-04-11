"""CL value exceptions module.

This module provides custom exceptions for CL value types.
"""


class ExceptionExceedMaxValue(Exception):
    """Exception raised when a number exceeds its maximum allowed value.

    This exception is raised when a number value is outside the valid range
    for its type (e.g., U32, I64, etc.).
    """

    def __init__(self, data: str, num_type: str, message: str = " isn't in the range of ") -> None:
        """Initialize the exception.

        Args:
            data: The value that exceeded the maximum.
            num_type: The type of number that was exceeded.
            message: The error message template.
        """
        self.data = data
        self.message = message
        self.num_type = num_type
        super().__init__(self.data + self.message + self.num_type)
