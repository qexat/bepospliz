# BePosPliz

BePosPliz (be positional please) is a lightweight module to anonymize the arguments of a function.

Relevant PEP: <https://peps.python.org/pep-0646>

I am not really sure if this has a real world purpose, but playing with new Python features is very enjoyable.
I appreciate the effort to improve type expressiveness, and I am looking forward to PEPs 695 and 696 for even more fun :D

## Features

### `anon_args`

#### Usage

Let the following function:

```py
from bepospliz import anon_args

@anon_args
def div(a: int, b: int) -> float:
    """Divide a by b"""
    return a / b
```

`div`'s original signature is `div(a: int, b: int) -> float`.

![`div` without decorator](https://raw.githubusercontent.com/qexat/bepospliz/main/docs/assets/div_original.png)

With the decorator `@anon_args`, it becomes `div(int, int) -> float`, meaning that it cannot be called by specifically naming the args anymore (e.g. `div(b=3, a=2)`)

![`div` with the decorator](https://raw.githubusercontent.com/qexat/bepospliz/main/docs/assets/div_anon_args.png)

---

#### Signature

```py
anon_args(function: Callable[[*Ps], R]) -> Callable[[*Ps], R]
```

with `Ps` being the set of types of `function`'s arguments, and `R` its return type.

**Example**

Given the previous `div` function, `Ps` would be `(int, int)` and `R` would be `float`.
