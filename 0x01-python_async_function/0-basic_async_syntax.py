#!/usr/bin/python3
import asyncio
import random
"""_Asyncio_
"""


async def wait_random(max_delay=10):
    """_asyncio_
    asyncio library in Python to create
    an asynchronous coroutine
    Args:
        max_delay (int, optional): _description_.
        Defaults to 10.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
