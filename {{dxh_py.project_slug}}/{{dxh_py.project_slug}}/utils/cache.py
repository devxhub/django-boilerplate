from django.core.cache import cache
from django.conf import settings
import hashlib
import json

class CacheManager:
    """
    Centralized Cache Manager to handle GET API caching and invalidation.
    """
    DEFAULT_TIMEOUT = getattr(settings, "CACHE_TTL", 3600)

    @staticmethod
    def generate_key(prefix, identifier=None, params=None):
        """
        Generates a predictable and unique cache key.
        Example: user_list:all or user_list:123:hashed_params
        """
        key = f"{prefix}"
        if identifier:
            key += f":{identifier}"
        
        if params:
            # Sort params to ensure consistent hashing
            sorted_params = json.dumps(params, sort_keys=True)
            hash_part = hashlib.md5(sorted_params.encode()).hexdigest()[:10]
            key += f":{hash_part}"
        
        return key

    @classmethod
    def get(cls, key):
        """Retrieve data from cache."""
        return cache.get(key)

    @classmethod
    def set(cls, key, data, timeout=None):
        """Store data in cache."""
        if timeout is None:
            timeout = cls.DEFAULT_TIMEOUT
        cache.set(key, data, timeout)

    @classmethod
    def delete(cls, key):
        """Invalidate a specific cache key."""
        cache.delete(key)

    @classmethod
    def clear_by_prefix(cls, prefix):
        """
        Clear all keys starting with a specific prefix.
        Requires django-redis backend for 'delete_pattern'.
        """
        if hasattr(cache, "delete_pattern"):
            cache.delete_pattern(f"{prefix}*")
        else:
            # Fallback if not using django-redis
            print("Warning: delete_pattern not supported by cache backend.")

    @classmethod
    def clear_all(cls):
        """Clear the entire cache."""
        cache.clear()
