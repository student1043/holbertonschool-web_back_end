#!/usr/bin/env python3
""" Async Comprehension """
import asyncio
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """ Async Comprehension """
    result = [i async for i in async_generator()]
    return result
