#!/usr/bin/env python3
'''Task 11's module.
'''


from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')

def safely_get_value(
    dct: Mapping,  
    key: Any, 
    default: Union[T, None] = None
) -> Union[Any, T]:
    '''Safely gets a value from the mapping or returns a default value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
