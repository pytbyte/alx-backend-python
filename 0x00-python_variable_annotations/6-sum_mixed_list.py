#!/usr/bin/env python3
'''mixed list sum
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Computes the sum of a list of integers and float.
    '''
    return float(sum(mxd_lst))
