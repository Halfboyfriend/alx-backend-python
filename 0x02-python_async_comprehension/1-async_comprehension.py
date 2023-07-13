#!/usr/bin/env python3
"""
TASK 1"""
from importlib import import_module as using
from typing import List


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Import async_generator from the previous task """
    return [num async for num in async_generator()]
