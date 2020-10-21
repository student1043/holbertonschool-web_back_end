#!/usr/bin/env python3.7
""" Async Generator """
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """ Async Generator """
    for i in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
