#!/usr/bin/python3
""" 0-basic_cache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ 0-basic_cache """
    def put(self, key, item):
        """ 0-basic_cache """
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ 0-basic_cache """
        if key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
