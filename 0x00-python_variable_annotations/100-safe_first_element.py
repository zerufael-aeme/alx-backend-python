#!/usr/bin/env python3
'''Task 10's module.
'''


from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    '''Returns the first element of a sequence or None if empty.
    '''
    if lst:
        return lst[0]
    else:
        return None
