#!/bin/bash/env python3
"""_async_generator_
"""
import asyncio
import random

async def async_generator():
    """
    Asynchronous generator function that produces random numbers with a 1-second delay.

    Yields:
        int: A random integer between 1 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)