#!/usr/bin/env python3
"""
Task 0 file
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Index Range
    """
    offset = (page - 1) * page_size
    return(offset, offset + page_size)
