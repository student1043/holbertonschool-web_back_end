#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Getting Hyper Index
        Trying to fix these errors
        before deadline
        hope it works!
        """
        assert (isinstance(index, int)
                and index in range(len(self.__indexed_dataset)))
        infolist = []
        count = 0
        indexer = index
        while count < page_size and indexer < len(self.__indexed_dataset):
            if indexer in self.__indexed_dataset:
                infolist.append(self.__indexed_dataset[indexer])
                indexer += 1
                count += 1
            else:
                indexer += 1
        if indexer < len(self.__indexed_dataset):
            nextindex = indexer
        else:
            nextindex = None
        infodict = {}
        infodict["index"] = index
        infodict["data"] = infolist
        infodict["page_size"] = len(infolist)
        infodict["next_index"] = nextindex
        infodict["page_size"] = len(infolist)
        infodict["data"] = infolist
        return infodict
