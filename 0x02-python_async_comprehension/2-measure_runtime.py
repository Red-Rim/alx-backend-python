#!/usr/bin/env python3
""" Async Comprehensions
"""


import time
import asyncio
from typing import Coroutine


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime"""
    start_time: float = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))  # type: Coroutine
    return time.time() - start_time
