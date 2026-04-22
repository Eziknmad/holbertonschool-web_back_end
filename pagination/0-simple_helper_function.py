#!/usr/bin/env python3
"""Module for simple pagination helper function."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end index for pagination parameters.

    Args:
        page: The current page number (1-indexed, first page is page 1).
        page_size: The number of items per page.

    Returns:
        A tuple containing the start index and end index corresponding
        to the range of indexes to return in a list for the given
        pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
