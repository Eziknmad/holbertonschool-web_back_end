#!/usr/bin/env python3
"""Module for key-value tuple creation with type annotations."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of a string and the square of a number as a float."""
    return (k, float(v ** 2))
