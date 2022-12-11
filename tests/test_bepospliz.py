import pytest

from bepospliz import anon_args


@anon_args
def poskwarg_func(a: int, b: float, c: str) -> bool:
    return str(float(a)) == str(b) == c


@anon_args
def varargs_func(*args: * tuple[int, float, str]) -> bool:
    a, b, c = args
    return str(float(a)) == str(b) == c


@anon_args
def kwonlyarg_func(*, a: int, b: float, c: str) -> bool:
    return str(float(a)) == str(b) == c


@anon_args
def kwargs_func(**kwargs: float) -> float:
    return sum(kwargs.values())


@pytest.mark.parametrize(
    "func",
    [
        poskwarg_func,
        varargs_func,
    ],
)
def test_anon_args_success(func):
    print(func)
    func(3, 3.0, "3.0")


@pytest.mark.parametrize(
    "func",
    [
        poskwarg_func,
        kwonlyarg_func,
        kwargs_func,
    ],
)
def test_anon_args_fail(func):
    with pytest.raises(TypeError):
        func(a=3, b=3.0, c="3.0")
