#!/usr/bin/env python3
'''Modules of task-56.
'''


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    '''Takes a list of floats and ints and returns their sum as a float.
    '''
    return float(sum(mxd_list))
