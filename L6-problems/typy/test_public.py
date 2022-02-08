# mypy: ignore-errors

import typing as tp

import mypy.api
import inspect
import tempfile


from .typy import func1, func2, func3, func4, func5


def check_annotations(func: tp.Callable[..., tp.Any]) -> None:
    for p, value in inspect.signature(func).parameters.items():
        assert value.annotation != inspect.Signature.empty, f"Parameter {p} does not have annotation"
        assert value.annotation != tp.Any, f"Parameter {p} has prohibited Any annotation"

    assert inspect.signature(func).return_annotation != inspect.Signature.empty, "Return does not have annotation"
    assert inspect.signature(func).return_annotation != tp.Any, "Return has prohibited Any annotation"


def check_func(func: tp.Callable[..., tp.Any], test_case: tp.Callable[..., tp.Any], is_success: bool) -> None:
    with tempfile.NamedTemporaryFile(mode="w") as fp:
        fp.write("import typing as tp")
        fp.write("\n")
        fp.write("import numbers")
        fp.write("\n")
        fp.write("import abc")
        fp.write("\n\n")
        fp.write(inspect.getsource(func))
        fp.write("\n")
        fp.write(inspect.getsource(test_case))
        fp.write("\n")
        fp.flush()

        normal_report, error_report, exit_status = mypy.api.run([fp.name, '--config-file', ''])
        print(f"Report:\n{normal_report}\n{error_report}")
        result_success_status = exit_status == 0
        assert result_success_status is is_success, \
            f"Mypy check should be {is_success}, but result {result_success_status}"


def func1_case_1() -> None:
    func1("dd")


def func1_case_2() -> None:
    func1(1j)


def func1_case_3() -> None:
    func1(1)


def func1_case_4() -> None:
    func1(1.0)


def func1_case_5() -> None:

    class R(float):
        pass

    func1(R(1))


def test_func1() -> None:
    check_annotations(func1)

    check_func(func1, func1_case_1, False)
    check_func(func1, func1_case_2, False)

    check_func(func1, func1_case_3, True)
    check_func(func1, func1_case_4, True)
    check_func(func1, func1_case_5, True)


def func2_case_1() -> None:
    func2(None)  # success


def func2_case_2() -> None:
    func2(True)  # success


def func2_case_3() -> None:
    func2(1.0)   # fail


def func2_case_4() -> None:
    func2("hello")   # success


def func2_case_5() -> None:
    func2(["hello"])  # fail


def func2_case_6() -> None:
    func2({1, 2, 3})  # fail


def func2_case_7() -> None:
    func2([1, 2, 3])  # success


def func2_case_8() -> None:
    func2([1.0, 2.0, 3.0])  # fail


def func2_case_9() -> None:
    func2({1: "hello"})  # fail


def func2_case_10() -> None:

    T = tp.TypeVar("T", int, str)

    class A(tp.Sequence[T]):
        def __init__(self, value: T):
            self._a: T = value

        @tp.overload  # noqa: F811
        def __getitem__(self, i: int) -> T:  # noqa: F811
            pass

        @tp.overload  # noqa: F811
        def __getitem__(self, s: slice) -> tp.Sequence[T]:  # noqa: F811
            pass

        def __getitem__(self, i):  # noqa: F811
            return self._a

        def __len__(self) -> int:
            pass

    func2(A[str]("hello"))  # fail


def func2_case_11() -> None:

    T = tp.TypeVar("T", bool, str)

    class A(tp.Sequence[T]):
        def __init__(self, value: T):
            self._a: T = value

        @tp.overload  # noqa: F811
        def __getitem__(self, i: int) -> T:   # noqa: F811
            pass

        @tp.overload  # noqa: F811
        def __getitem__(self, s: slice) -> tp.Sequence[T]:  # noqa: F811
            pass

        def __getitem__(self, i):  # noqa: F811
            return self._a

        def __len__(self) -> int:
            pass

    func2(A[bool](True))  # success


def test_func2() -> None:
    check_annotations(func2)

    check_func(func2, func2_case_1, True)
    check_func(func2, func2_case_2, True)
    check_func(func2, func2_case_3, False)
    check_func(func2, func2_case_4, True)
    check_func(func2, func2_case_5, False)
    check_func(func2, func2_case_6, False)
    check_func(func2, func2_case_7, True)
    check_func(func2, func2_case_8, False)
    check_func(func2, func2_case_9, False)
    check_func(func2, func2_case_10, False)
    check_func(func2, func2_case_11, True)


def func3_case_1() -> None:
    func3((1, "re", "rt", ["a", "b", "c"]))  # success


def func3_case_2() -> None:
    func3((1, "re", "rt", "hello"))  # success


def func3_case_3() -> None:
    func3((True, "re", "rt", "hello"))  # success


def func3_case_4() -> None:
    func3((True, "re", "rt", "hello"))  # success


def func3_case_5() -> None:
    func3((True, "re", "rt", "hello", "hi"))  # fail


def func3_case_6() -> None:
    class A(str):
        pass

    func3((True, A(), A(), A()))  # success


def func3_case_7() -> None:
    class A(str):
        pass

    func3((True, "re", "rt", "hello", A()))  # fail


def func3_case_8() -> None:
    func3((1.1, "", "", "hello"))  # success


def func3_case_9() -> None:
    func3((1j, "", "", "hello"))  # fail


def test_func3() -> None:
    check_annotations(func3)

    check_func(func3, func3_case_1, True)
    check_func(func3, func3_case_2, True)
    check_func(func3, func3_case_3, True)
    check_func(func3, func3_case_4, True)
    check_func(func3, func3_case_5, False)
    check_func(func3, func3_case_6, True)
    check_func(func3, func3_case_7, False)
    check_func(func3, func3_case_8, True)
    check_func(func3, func3_case_9, False)


def func4_case_1() -> None:
    func4((1, 1, 2, 4))  # success


def func4_case_2() -> None:
    func4((1,))  # success


def func4_case_3() -> None:
    func4((1.2, 3.4))  # success


def func4_case_4() -> None:
    func4((1j, 3j, 6j, 7j))  # fail


def func4_case_5() -> None:
    func4((True, False))  # success


def func4_case_6() -> None:
    func4(("there", "are", "no", "reason"))  # fail


def test_func4() -> None:
    check_annotations(func4)

    check_func(func4, func4_case_1, True)
    check_func(func4, func4_case_2, True)
    check_func(func4, func4_case_3, True)
    check_func(func4, func4_case_4, False)
    check_func(func4, func4_case_5, True)
    check_func(func4, func4_case_6, False)


def func5_case_1() -> None:

    def f(a: float, b: float, c: complex) -> int:
        return 1

    func5(f, 1, 4.5, 1j)  # success


def func5_case_2() -> None:

    def f(a: complex, b: complex, c: complex) -> bool:
        return True

    func5(f, 1, 4, True)  # success


def func5_case_3() -> None:

    def f(a: bool, b: float, c: complex) -> int:
        return 1

    func5(f, 1, 4.5, 1j)  # false


def func5_case_4() -> None:

    def f(a: int, b: int, c: complex) -> int:
        return 1

    func5(f, 1, 4.5, 1j)  # false


def func5_case_5() -> None:

    def f(a: int, b: float, c: float) -> int:
        return 1

    func5(f, 1, 4.5, 1j)  # false


def func5_case_6() -> None:

    def f(a: float, b: float, c: complex) -> float:
        return 1.0

    func5(f, True, True, True)  # success


def func5_case_7() -> None:

    def f(a: float, b: float, c: complex) -> complex:
        return 1j

    func5(f, True, True, True)  # false


def test_func5() -> None:
    check_annotations(func5)

    check_func(func5, func5_case_1, True)
    check_func(func5, func5_case_2, True)
    check_func(func5, func5_case_3, False)
    check_func(func5, func5_case_4, False)
    check_func(func5, func5_case_5, False)
    check_func(func5, func5_case_6, True)
    check_func(func5, func5_case_7, False)
