#!/usr/bin/env python3
import csv
import math
from typing import List
"""
Task 1 file
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Index Range
    """
    offset = (page - 1) * page_size
    return(offset, offset + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        myindexing = index_range(page, page_size)
        self.dataset()
        return self.__dataset[myindexing[0]:myindexing[1]]
        if IndexError:
            return []
