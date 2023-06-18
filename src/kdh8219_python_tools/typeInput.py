from typing import Optional, Callable, TypeVar

T = TypeVar('T')
def type_input(func: Callable[[str],T] = int, errorMessage: Optional[str] = "", *args, **kwargs) -> T:
    while True:
        try:
            return func(input(*args, **kwargs))
        except ValueError:
            if errorMessage != None:
                print(errorMessage)
            continue

def int_input(errorMessage: Optional[str] = "", *args, **kwargs) -> int:
    return type_input(int, errorMessage, *args, **kwargs)

def float_input(errorMessage: Optional[str] = "", *args, **kwargs) -> float:
    return type_input(float, errorMessage, *args, **kwargs)

