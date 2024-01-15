#!/usr/bin/env python3
'''Task_wait_random
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns task_wait_random n
    times with the specified max_delay.

    :param n: Number of times to spawn.
    :param max_delay: Maximum delay in seconds.
    :return: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    task_outcome = await asyncio.gather(*tasks)
    task_outcome_ascending = sorted(task_outcome)
    return task_outcome_ascending
