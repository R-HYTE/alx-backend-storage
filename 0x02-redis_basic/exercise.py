#!/usr/bin/env python3
"""
Cache module to interact with Redis for storing and retrieving data.
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class to handle storage and retrieval of data in Redis.

    Attributes:
        _redis (redis.Redis): Instance of the Redis client.
    """

    def __init__(self):
        """
        Initialize the Cache class.

        Creates an instance of the Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key (str): The key to retrieve from Redis.
            fn (Optional[Callable]): A callable function to convert the data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data,
            optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data
