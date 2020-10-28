#!/usr/bin/env python3
"""
Task 0 file
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Index Range
    """
    if page is 1:
        return (page * 0, page * page_size)
    return (page * 10, page * page_size)
