#!/usr/bin/env python3
"""
Task 11
"""
from typing import Dict, Any, TypeVar, Mapping, Union

K = TypeVar('K')
Result = Union[Any, K]
Dev = Union[K, None]


def safely_get_value(dc: Mapping, key: Any, default: Dev = None) -> Result:
    """

    :param dct:
    :param key:
    :param default:
    :return:
    """
    if key in dc:
        return dc[key]
    else:
        return default
