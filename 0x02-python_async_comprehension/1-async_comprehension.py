#!/usr/bin/env python3
'''async_generator module.
'''
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 random numbers from a 10- random
       number generator.
    '''
    return [i async for i in async_generator()]
