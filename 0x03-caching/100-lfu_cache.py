#!/usr/bin/python3
import collections
from collections import Counter
"""
LFU Task
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Class
    """

    def __init__(self):
        """
        LFU INIT
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        LFU PUT
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    print("DISCARD:", self.queue.index(Counter(self.queue).most_common()[:-1:3]))
                    save = self.queue.pop(self.queue.index(Counter(self.queue).most_common()[:-1:3]))
                    del self.cache_data[save]
                self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        LFU GET
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
