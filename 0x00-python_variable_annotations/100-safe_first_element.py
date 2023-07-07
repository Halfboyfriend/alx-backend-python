#!/usr/bin/env python3
"""
Task 10
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """

    :param lst:
    :return:
    """
    if lst:
        return lst[0]
    else:
        return None
