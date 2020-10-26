#!/usr/bin/python3
"""
LIFO Task
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Class
    """

    def __init__(self):
        """
        LIFO Testing
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        LIFO Tester
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.queue[len(self.queue) - 1]]
                    print("DISCARD:", self.queue[len(self.queue) - 1])
                    self.queue.pop(len(self.queue) - 1)
                self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        LIFO GET
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
