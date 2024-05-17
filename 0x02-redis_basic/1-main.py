#!/usr/bin/env python3
"""
Main file for testing the Cache class.
"""

from exercise import Cache

def main():
    """
    Main function to test the Cache class.
    """
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        retrieved_value = cache.get(key, fn=fn)
        assert retrieved_value == value, f"Test failed: {retrieved_value} != {value}"

    print("All tests passed!")

if __name__ == "__main__":
    main()
