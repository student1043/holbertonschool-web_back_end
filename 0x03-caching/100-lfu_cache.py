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
        self.tracking = []

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
                    print("DISCARD:", (Counter(self.tracking).most_common()[0][0]))
                    save = self.queue.pop(self.queue.index(Counter(self.tracking).most_common()[0][0]))
                    del self.cache_data[save]
                    self.tracking.pop(self.tracking.index(Counter(self.tracking).most_common()[0][0]))
                self.cache_data[key] = item
            self.queue.append(key)
            self.tracking.append(key)

    def get(self, key):
        """
        LFU GET
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
