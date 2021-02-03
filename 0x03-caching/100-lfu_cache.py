#!/usr/bin/python3
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
                    keys = []
                    values = []
                    for k, v in sorted(self.cache_data.items(),
                                   key=lambda x: x[1]):
                        keys.append(k)
                        values.append(v)
                    index = values.index(min(values))
                    least_freq = keys[index]
                    del self.cache_data[least_freq]
                    print("DISCARD: {}".format(least_freq))
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
