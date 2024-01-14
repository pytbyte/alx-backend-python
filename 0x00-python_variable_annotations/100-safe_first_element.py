#!/usr/bin/env python3
'''first present
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Retrieves the first element of a sequence if it exists.
    '''
    return lst[0] if lst else None
