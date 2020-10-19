#!/usr/bin/env python3
""" Element Length """
from typing import Sequence, Tuple, Union, List, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
