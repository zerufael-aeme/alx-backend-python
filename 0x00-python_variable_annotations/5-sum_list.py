#!/usr/bin/env python3
'''Modules of task-5.
'''


def sum_list(input_list: list[float]) -> float:
    '''Takes a list of floats and returns their sum as a float
    '''
    sum: float = 0
    for num in input_list:
        sum += num
    return sum
