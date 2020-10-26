#!/usr/bin/python3
"""
MRU Task
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Class
    """

    def __init__(self):
        """
        MRU INIT
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        MRU PUT
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    print("DISCARD:", self.queue[-1])
                    save = self.queue.pop(-1)
                    del self.cache_data[save]
                self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        MRU GET
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
