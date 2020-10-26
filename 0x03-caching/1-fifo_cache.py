#!/usr/bin/python3
""" FIFO """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO """

    def __init__(self):
        """ FIFO """
        super().__init__()
        self.tab = []

    def put(self, key, item):
        """ FIFO """
        if key is not None and item is not None:
            self.tab.append(key)
            if key in self.cache_data:
                self.cache_data[key] = item
                self.tab.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.tab[0]]
                    print("DISCARD:", self.tab[0])
                    self.tab.pop(0)
                self.cache_data[key] = item

    def get(self, key):
        """ FIFO """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
