#!/usr/bin/env python3
'''Modules of task-7.
'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a tuple
    '''
    return (k, float(v*v))
