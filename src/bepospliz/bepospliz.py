"""
BePosPliz (be positional please) is a lightweight module to anonymize the args of a function.

Relevant PEP: <https://peps.python.org/pep-0646>

I am not really sure if this has a real world purpose, but playing with new Python features is very enjoyable.
I appreciate the effort to improve type expressiveness, and I am looking forward to PEPs 695 and 696 for even more fun :D
"""

import functools
from collections.abc import Callable
from typing import TypeVar
from typing import TypeVarTuple

__all__ = ("anon_args",)

Ps = TypeVarTuple("Ps")
R = TypeVar("R")


def anon_args(function: Callable[[*Ps], R]) -> Callable[[*Ps], R]:
    """
    Make `function` args anonymous. Supports functions with every kind of argument except keyword.

    Example:
    ```
    # fib signature: fib(int) -> int
    >>> @anon_args
    ... def fib(n: int) -> int:
    ...     if n <= 1:
    ...         return n
    ...     return fib(n - 2) + fib(n - 1)

    >>> fib(n=2) # typing-time AND runtime error
    ```
    """

    @functools.wraps(function)
    def inner(*args: * tuple[*Ps]) -> R:
        return function(*args)

    return inner
