#!/usr/bin/env python3
'''Task 9's module.
'''


from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list
    '''
    return [(i, len(i)) for i in lst]
