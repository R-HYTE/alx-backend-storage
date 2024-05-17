#!/usr/bin/env python3
"""
Cache module to interact with Redis for storing and retrieving data.
"""

from functools import wraps
import redis
import uuid
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: Decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to count method calls and execute the original method.

        Args:
            self: The instance of the class.
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        Returns:
            Any: Result of the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    @count_calls
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
        self._redis.lpush("{}:inputs".format(self.store.__qualname__), data)
        self._redis.lpush("{}:outputs".format(self.store.__qualname__), key)
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

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            Optional[str]: Retrieved string or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            Optional[int]: Retrieved integer or None if the key does not exist.
        """
        return self.get(key, fn=int)
