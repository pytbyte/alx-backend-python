#!/usr/bin/env python3
"""Utilities for managing GitHub organization client."""
import requests
from functools import wraps
from typing import Mapping, Sequence, Any, Dict, Callable

__all__ = [
    "access_nested_map",
    "get_json_data",
    "memoize_method",
]


def access_nested_map(nested_map: Mapping, key_path: Sequence) -> Any:
    """Access a nested map using a key path.

    Parameters:
    - nested_map: Mapping
        A nested map
    - key_path: Sequence
        A sequence of keys representing a path to the value

    Example:
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in key_path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map


def get_json_data(url: str) -> Dict:
    """Fetch JSON data from a remote URL."""
    response = requests.get(url)
    return response.json()


def memoize_method(method: Callable) -> Callable:
    """Decorator to memoize a method.

    Example:
    class MyClass:
        @memoize_method
        def some_method(self):
            print("some_method called")
            return 42

    >>> my_object = MyClass()
    >>> my_object.some_method
    some_method called
    42
    >>> my_object.some_method
    42
    """
    attribute_name = "_{}".format(method.__name__)

    @wraps(method)
    def memoized(self):
        """Wrapper function for memoization."""
        if not hasattr(self, attribute_name):
            setattr(self, attribute_name, method(self))
        return getattr(self, attribute_name)

    return property(memoized)
