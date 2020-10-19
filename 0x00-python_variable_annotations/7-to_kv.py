#!/usr/bin/env python3
""" Return Tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return Tuple """
    return(k, v**2)
