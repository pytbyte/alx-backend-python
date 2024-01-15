#!/usr/bin/env python3
'''__Asyncio_task__
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns an asyncio.Task.

    :param max_delay: Maximum delay in seconds.
    :return: asyncio.Task
    """
    # Creating an asyncio.Task for wait_random with the specified max_delay
    task = asyncio.create_task(wait_random(max_delay))
    return task
