#!/usr/bin/python3
""" FIFO """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO """

    def __init__(self):
        """ FIFO """
        super().__init__()
        self.mylisting = []

    def put(self, key, item):
        """ FIFO """
        if key is not None and item is not None:
            self.mylisting.append(key)
            if key in self.cache_data:
                self.cache_data[key] = item
                self.mylisting.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.mylisting[0]]
                    print("DISCARD: {}".format(self.mylisting[0]))
                    self.mylisting.pop(0)
                self.cache_data[key] = item

    def get(self, key):
        """ FIFO """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
