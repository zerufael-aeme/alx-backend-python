#!/usr/bin/env python3
'''Modules of task-7.
'''


from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    '''returns a tuple
    '''
    return (k, float(v*v))
