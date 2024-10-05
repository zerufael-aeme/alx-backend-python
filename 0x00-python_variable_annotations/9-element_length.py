#!/usr/bin/env python3
'''Task 9's module.
'''


from typing import Iterable, List


def element_length(lst: Iterable) -> List:
    return [(i, len(i)) for i in lst]
