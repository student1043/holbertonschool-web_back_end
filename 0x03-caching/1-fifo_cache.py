#!/usr/bin/python3
"""
FIFO Task
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Class
    """

    def __init__(self):
        """
        FIFO Testing
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        FIFO Tester
        """
        if key is not None and item is not None:
            self.queue.append(key)
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.queue[0]]
                    print("DISCARD:", self.queue[0])
                    self.queue.pop(0)
                self.cache_data[key] = item

    def get(self, key):
        """
        FIFO GET
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
