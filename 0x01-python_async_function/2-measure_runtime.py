#!/usr/bin/env python3
'''runtime measure
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    :param n: Number of times to spawn wait_random.
    :param max_delay: Maximum delay in seconds.
    :return: Average execution time per wait_random call.
    """
    commence_ = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_ = time.time()
    duration_ = end_ - commence_

    average_duration = duration_ / n
    return average_duration
