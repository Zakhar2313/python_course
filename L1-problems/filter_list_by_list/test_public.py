import copy
import dataclasses
import dis
import typing as tp

import pytest


from .filter_list_by_list import filter_list_by_list


@dataclasses.dataclass
class Case:
    a: tp.Sequence[int]
    b: tp.Sequence[int]
    result: tp.Sequence[int]

    def __str__(self) -> str:
        return 'filter_{}_by_{}'.format(self.a, self.b)


TEST_CASES = [
    Case(a=[], b=[], result=[]),
    Case(a=[1, 2, 3], b=[], result=[1, 2, 3]),
    Case(a=[], b=[1, 2, 3], result=[]),
    Case(a=[], b=[1], result=[]),
    Case(a=[1], b=[], result=[1]),
    Case(a=[1], b=[1], result=[]),
    Case(a=[1, 2], b=[3, 4], result=[1, 2]),
    Case(a=[1, 3], b=[2, 4], result=[1, 3]),
    Case(a=[3, 4], b=[1, 2], result=[3, 4]),
    Case(a=[1, 3], b=[2, 4], result=[1, 3]),
    Case(a=[2, 3], b=[1, 2], result=[3]),
    Case(a=[1, 1], b=[1, 1], result=[]),
    Case(a=[1, 2], b=[1, 1], result=[2]),
    Case(a=[1, 2], b=[1, 2], result=[]),
    Case(a=[2, 3], b=[1, 4], result=[2, 3]),
    Case(a=[1, 4], b=[4, 4], result=[1]),
    Case(a=range(10**5), b=[0] * 10**5, result=list(range(1, 10**5)))
]


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_get_middle_value(t: Case) -> None:
    given_a = copy.deepcopy(t.a)
    given_b = copy.deepcopy(t.b)

    answer = filter_list_by_list(t.a, t.b)

    assert t.a == given_a, "You shouldn't change inputs"
    assert t.b == given_b, "You shouldn't change inputs"

    is_used_build_set = any(i.argval == 'set' for i in dis.get_instructions(filter_list_by_list))
    assert not is_used_build_set, "You should use iteration ONLY, not building sets"

    assert answer == t.result
