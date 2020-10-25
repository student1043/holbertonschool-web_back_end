#!/usr/bin/python3
""" 0-basic_cache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ 0-basic_cache """
    def put(self, key, item):
        """ 0-basic_cache """
        super(BasicCache, self).put(key, item)
        if key or item is None:
            pass
        else:
            self.cache_data['key'] = item

    def get(self, key):
        """ 0-basic_cache """
        super(BasicCache, self).get(key)
        if key or self.cache_data[key] is None:
            return None
        else:
            return self.cache_data[key]
