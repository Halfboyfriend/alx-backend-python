#!/usr/bin/env python3
# Write a type-annotated function sum_mixed_list
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    :param mxd_lst:
    :return:
    """
    return sum(mxd_lst)
