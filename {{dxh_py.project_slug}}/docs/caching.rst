Caching
=======

This boilerplate includes a centralized caching architecture to improve performance and reduce database load.

Configuration
-------------

The caching settings are located in ``config/settings/base.py``. By default, it is configured to use Redis.

* **Backend**: Django Redis
* **Default Timeout**: 1 hour (3600 seconds)

You can customize the timeout in your environment variables:

.. code-block:: bash

    CACHE_TTL=3600

Usage
-----

To use caching in your views or services, use the ``CacheManager`` utility.

Caching GET Requests
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from {{dxh_py.project_slug}}.utils.cache import CacheManager
    from rest_framework.response import Response

    def list(self, request, *args, **kwargs):
        cache_key = CacheManager.generate_key(
            prefix="item_list",
            identifier=request.user.id,
            params=request.query_params.dict()
        )

        cached_data = CacheManager.get(cache_key)
        if cached_data:
            return Response(cached_data)

        # Fetch from DB and save to cache
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        CacheManager.set(cache_key, serializer.data)

        return Response(serializer.data)

Cache Invalidation
~~~~~~~~~~~~~~~~~~

When data is modified (POST/PUT/PATCH/DELETE), invalidate the related cache:

.. code-block:: python

    def perform_update(self, serializer):
        instance = serializer.save()
        CacheManager.clear_by_prefix(f"item_list:{instance.id}")

Management Commands
-------------------

You can manage the cache using the ``clear_cache`` management command:

* **Clear all cache**:
  .. code-block:: bash

      python manage.py clear_cache --all

* **Clear by prefix**:
  .. code-block:: bash

      python manage.py clear_cache --prefix=item_list

* **Clear specific key**:
  .. code-block:: bash

      python manage.py clear_cache --key=item_list:123
