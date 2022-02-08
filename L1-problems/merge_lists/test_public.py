import copy
import dataclasses
import dis

import typing as tp

import pytest


from .merge_lists import merge


@dataclasses.dataclass
class Case:
    a: tp.Sequence[int]
    b: tp.Sequence[int]
    result: tp.Sequence[int]

    def __str__(self) -> str:
        return 'merge_{}_{}'.format(self.a, self.b)


TEST_CASES = [
    Case(a=[], b=[], result=[]),
    Case(a=[1, 2, 3], b=[], result=[1, 2, 3]),
    Case(a=[], b=[1, 2, 3], result=[1, 2, 3]),
    Case(a=[], b=[1], result=[1]),
    Case(a=[1], b=[], result=[1]),
    Case(a=[1], b=[1], result=[1, 1]),
    Case(a=[1, 2], b=[3, 4], result=[1, 2, 3, 4]),
    Case(a=[1, 3], b=[2, 4], result=[1, 2, 3, 4]),
    Case(a=[3, 4], b=[1, 2], result=[1, 2, 3, 4]),
    Case(a=[1, 3], b=[2, 4], result=[1, 2, 3, 4]),
    Case(a=[2, 3], b=[1, 2], result=[1, 2, 2, 3]),
    Case(a=[1, 1], b=[1, 1], result=[1, 1, 1, 1]),
    Case(a=[1, 2], b=[1, 1], result=[1, 1, 1, 2]),
    Case(a=[1, 2], b=[1, 2], result=[1, 1, 2, 2]),
    Case(a=[2, 3], b=[1, 4], result=[1, 2, 3, 4]),
    Case(a=[1, 4], b=[4, 4], result=[1, 4, 4, 4]),
]


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_get_middle_value(t: Case) -> None:
    given_a = copy.deepcopy(t.a)
    given_b = copy.deepcopy(t.b)

    answer = merge(t.a, t.b)

    assert t.a == given_a, "You shouldn't change inputs"
    assert t.b == given_b, "You shouldn't change inputs"

    is_used_sorted = any(i.argval == 'sorted' for i in dis.get_instructions(merge))
    assert not is_used_sorted, "You should use iteration ONLY, not manually sorting"

    is_used_build_slice = any(i.opname == 'BUILD_SLICE' for i in dis.get_instructions(merge))
    assert not is_used_build_slice, "You should use iteration ONLY, not slicing"

    assert answer == t.result
