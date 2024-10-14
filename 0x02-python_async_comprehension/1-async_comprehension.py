#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import Generator, List


async_generator = __import__("0-async_generator.py").async_generator


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from a 10-number generator.
    '''
    randoms = [i async for i in async_generator()]
