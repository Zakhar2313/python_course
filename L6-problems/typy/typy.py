# WARNING: don't add additional imports and functions

import typing as tp


def func1(a: float) -> float:
    return a / 2


def func2(a: tp.Optional[tp.Union[tp.Sequence[int], tp.Sequence[bool], bool, str]]) -> tp.Optional[bool]:
    if a is None:
        return None
    else:
        return bool(a)


def func3(a: tp.Tuple[float,
                      tp.Union[str, tp.Callable[[str], None]],
                      tp.Union[str, tp.Callable[[str], None]],
                      tp.Union[str, tp.Sequence[str]]]) -> tp.Union[str, tp.Callable[[str], None]]:
    return a[1]


def func4(a: tp.Tuple[float, ...]) -> tp.Optional[float]:
    if a:
        return a[0]
    return None


def func5(a: tp.Callable[[float, float, complex], float], b: float, c: float, d: complex) -> float:
    return a(b, c, d)
