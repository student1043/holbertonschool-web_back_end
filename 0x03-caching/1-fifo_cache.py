#!/usr/bin/python3
""" FIFO """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO """
    def __init__(self):
        """ constructor """
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
                if len(self.cache_data) > self.MAX_ITEMS - 1:
                    del self.cache_data[self.tab[0]]
                    print("DISCARD: {}".format(self.tab[0]))
                    self.tab.pop(0)
                self.cache_data[key] = item

    def get(self, key):
        """ FIFO """
        if key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
