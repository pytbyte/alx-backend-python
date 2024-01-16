import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    launch_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - launch_time

    return total_runtime

if __name__ == "__main__":
    total_runtime = asyncio.run(measure_runtime())
    print(f"Total runtime: {total_runtime:.2f} seconds")
