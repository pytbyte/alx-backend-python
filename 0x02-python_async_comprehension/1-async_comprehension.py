#!/usr/bin/env python3
"""_async_comprehension_
"""
import asyncio
from typing import List

async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_async_comprehension_
    collect 10 random numbers using an async
    comprehensing over async_generator

    return:
        10 random numbers collected.

    """
    result = []
    async for i in async_gen():
        result.append(i)
    return result
