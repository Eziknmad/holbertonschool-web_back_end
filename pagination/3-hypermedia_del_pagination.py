#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize a new Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Return the dataset indexed by original position.

        Returns:
            A dictionary where each key is the original index of a row
            and each value is the corresponding dataset row.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient hypermedia page.

        Args:
            index: The starting index of the page.
            page_size: The number of items to return.

        Returns:
            A dictionary containing:
            - index: the current start index
            - data: the page of dataset rows
            - page_size: the number of rows returned
            - next_index: the next index to query with

        Raises:
            AssertionError: If index is not within a valid range or
            page_size is not a positive integer.
        """
        if index is None:
            index = 0

        assert type(index) is int and 0 <= index < len(self.dataset())
        assert type(page_size) is int and page_size > 0

        indexed_dataset = self.indexed_dataset()
        data = []
        next_index = index
        dataset_length = len(self.dataset())

        while len(data) < page_size and next_index < dataset_length:
            row = indexed_dataset.get(next_index)
            if row is not None:
                data.append(row)
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
