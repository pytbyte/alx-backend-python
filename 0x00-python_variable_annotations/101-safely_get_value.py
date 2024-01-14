#!/usr/bin/env python3
'''get value
'''
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    '''Retrieves a value from a dict using a given key.
    '''
    return dct.get(key, default)
