#!/usr/bin/env python3
'''Task 11's module.
'''


from typing import Sequence, Any, Optional, Mapping, TypeVar, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None]) -> Optional[Union[Any, T]]:
    '''Properly Annotated
    '''
    if key in dct:
        return dct[key]
    else:
        return default
