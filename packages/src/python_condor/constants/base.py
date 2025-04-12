"""Base constants module.

This module provides base classes and utilities for defining constants
used throughout the Casper network SDK.
"""

from enum import Enum
from typing import Any, Callable, TypeVar

T = TypeVar('T')


class NoneHolder:
    """A class that holds nothing.

    This class is used as a placeholder for None values in certain contexts
    where None itself cannot be used.
    """
    pass


class TAG(Enum):
    """Enumeration of CL (Casper) type tags.

    This enum defines numeric tags used to identify different types
    in the Casper network's type system.
    """
    CLBool = 0
    CLI32 = 1
    CLI64 = 2
    CLU8 = 3
    CLU32 = 4
    CLU64 = 5
    CLU128 = 6
    CLU256 = 7
    CLU512 = 8
    CLUnit = 9
    CLString = 10
    CLKey = 11
    CLURef = 12
    CLOption = 13
    CLList = 14
    CLByteArray = 15
    CLResult = 16
    CLMap = 17
    CLTuple1 = 18
    CLTuple2 = 19
    CLTuple3 = 20
    CLAny = 21
    CLPublicKey = 22


class Length(Enum):
    """Enumeration of tuple lengths.

    This enum defines the valid lengths for CL tuple types.
    """
    CLTuple1 = 1
    CLTuple2 = 2
    CLTuple3 = 3


def constant(f: Callable[..., T]) -> property:
    """Decorator for creating read-only properties.

    This decorator is used to create read-only properties that return
    constant values. Attempting to set the property will raise a TypeError.

    Args:
        f: A function that returns the constant value.

    Returns:
        A property that can only be read, not written to.
    """

    def fset(self: Any, value: Any) -> None:
        raise TypeError("Cannot modify a constant value")

    def fget(self: Any) -> T:
        return f()

    return property(fget, fset)
