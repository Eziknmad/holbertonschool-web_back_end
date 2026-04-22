#!/usr/bin/env python3
"""Module that provides hypermedia pagination on a CSV dataset."""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes for a pagination request.

    Args:
        page: The page number starting from 1.
        page_size: The number of items to return per page.

    Returns:
        A tuple containing the start index and end index for the page.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize a new Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Load and cache the dataset from the CSV file.

        Returns:
            The dataset as a list of rows without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return a page of the dataset corresponding to the given arguments.

        Args:
            page: The page number starting from 1.
            page_size: The number of items to return per page.

        Returns:
            A list of rows corresponding to the requested page. If the page
            is out of range, an empty list is returned.

        Raises:
            AssertionError: If page or page_size is not an integer greater
            than 0.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary containing hypermedia pagination information.

        Args:
            page: The page number starting from 1.
            page_size: The number of items to return per page.

        Returns:
            A dictionary containing the following keys:
            page_size: the length of the returned dataset page.
            page: the current page number.
            data: the dataset page as a list of rows.
            next_page: the number of the next page or None if no next page.
            prev_page: the number of the previous page or None if no prev.
            total_pages: the total number of pages in the dataset.
        """
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
