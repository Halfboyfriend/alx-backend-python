#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """

    :param multiplier:
    :return:
    """
    def multiplier_fn(value: float) -> float:
        """

        :param value:
        :return:
        """
        return value * multiplier
    return multiplier_fn
