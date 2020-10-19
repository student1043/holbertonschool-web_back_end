#!/usr/bin/env python3
""" Element Length """
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Element Length """
    if lst:
        return lst[0]
    else:
        return None
