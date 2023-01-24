#!/usr/bin/env python3
"""
    basic caching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        represents an object that allows storing and
        retrieving items from a dictionary
    """

    def put(self, key, item):
        """
            adds an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
            retrieves an item by key
        """
        return self.cache_data.get(key, None)
