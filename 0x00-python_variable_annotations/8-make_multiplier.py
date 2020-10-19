#!/usr/bin/env python3
""" Multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multiplier """
    def multiply(number: float):
        """ Multiplier """
        return number * multiplier
    return multiply
