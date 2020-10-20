#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    '''
    Test file for printing the correct output of the wait_n coroutine
    '''
    loop = asyncio.get_event_loop()
    return(loop.create_task)
