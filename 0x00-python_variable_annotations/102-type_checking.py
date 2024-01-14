#!/usr/bin/env python3
'''zoom
'''
from typing import List, Tuple, TypeVar

T = TypeVar('T')

def zoom_array(lst: Tuple[T], factor: int = 2) -> List[T]:
    '''Creates multiple copies of items in a tuple.
    '''
    return list(lst) * factor

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
