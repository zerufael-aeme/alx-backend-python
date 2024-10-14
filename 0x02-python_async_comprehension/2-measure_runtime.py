#!/usr/bin/env python3
'''Task 2's module.
'''
import time
import asyncio
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    return time.time() - start_time
