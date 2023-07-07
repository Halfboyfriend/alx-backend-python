#!/usr/bin/env python3
"""
Task 12
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """

    :param lst:
    :param factor:
    :return:
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in