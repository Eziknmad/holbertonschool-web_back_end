#!/usr/bin/env python3
"""Module for function multiplier with type annotations."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiply(x: float) -> float:
        """Multiply x by the multiplier."""
        return x * multiplier
    return multiply
