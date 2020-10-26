#!/usr/bin/python3
"""
LRU Task
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Class
    """

    def __init__(self):
        """
        LRU INIT
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        LRU PUT
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    print("DISCARD:", self.queue[0])
                    save = self.queue.pop(0)
                    del self.cache_data[save]
                self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        LRU GET
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
