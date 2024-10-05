#!/usr/bin/env python3
'''Modules of task-6.
'''


from typing import List


def sum_mixed_list(mxd_list: List[float | int]) -> float:
    '''Takes a list of floats and ints and returns their sum as a float.
    '''
    return float(sum(mxd_list))
