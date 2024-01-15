#!/usr/bin/python3
import asyncio
import random
"""_Asyncio_
"""


async def wait_random(max_delay=10) -> float:
    """_asyncio_
    Asynchronous coroutine that waits for a random delay.
    :param max_delay: Maximum delay in seconds (default is 10).
    :return: Random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
