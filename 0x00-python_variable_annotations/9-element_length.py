#!/usr/bin/env python3
from typing import List, Tuple
def element_length(lst: List[int]) -> Tuple[int]:
    return [(i, len(i)) for i in lst]