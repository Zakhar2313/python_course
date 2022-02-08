import copy
import dataclasses
import typing as tp

import pytest


from .min_to_drop import get_min_to_drop


@dataclasses.dataclass
class Case:
    a: tp.Sequence[tp.Any]
    result: int

    def __str__(self) -> str:
        return 'reverse_{}'.format(self.a)


TEST_CASES = [
    Case(a=[], result=0),
    Case(a=[1, 2, 3, 1], result=2),
    Case(a=[1, 2, 1], result=1),
    Case(a=[1, 1], result=0),
    Case(a=[1], result=0),
    Case(a=["a"], result=0),
    Case(a=["a", "a"], result=0),
    Case(a=["a", "a", "b", "c"], result=2),
    Case(a=[1, 2, 3, 4], result=3),
    Case(a=[1, 2, 3, 4, 5, 6, 1], result=5),
]


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_min_to_drop(t: Case) -> None:
    given_a = copy.deepcopy(t.a)

    answer = get_min_to_drop(given_a)

    assert t.a == given_a, "You shouldn't change inputs"
    assert answer == t.result
