import copy
import dis
import dataclasses
import typing as tp

import pytest


from .reverse_list import reverse, reverse_inplace


@dataclasses.dataclass
class Case:
    a: tp.MutableSequence[int]
    result: tp.MutableSequence[int]

    def __str__(self) -> str:
        return 'reverse_{}'.format(self.a)


TEST_CASES = [
    Case(a=[], result=[]),
    Case(a=[1, 2, 3], result=[3, 2, 1]),
    Case(a=[1, 2, 1], result=[1, 2, 1]),
    Case(a=[1, 2, 3, 4], result=[4, 3, 2, 1]),
    Case(a=[1], result=[1]),
    Case(a=[2, 2, 2, 2], result=[2, 2, 2, 2]),
]


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_reverse(t: Case) -> None:
    given_a = copy.deepcopy(t.a)

    answer = reverse(given_a)

    assert t.a == given_a, "You shouldn't change inputs"

    is_used_reversed = any(i.argval == 'reversed' for i in dis.get_instructions(reverse))
    assert not is_used_reversed, "You shouldn't use reversed function"

    is_used_build_slice = any(i.opname == 'BUILD_SLICE' for i in dis.get_instructions(reverse))
    assert not is_used_build_slice, "You should use iteration ONLY, not slicing"

    assert answer == t.result


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_reverse_inplace(t: Case) -> None:
    given_a = copy.deepcopy(t.a)

    reverse_inplace(given_a)

    is_used_reverse = any(i.argval == 'reverse' for i in dis.get_instructions(reverse_inplace))
    assert not is_used_reverse, "You shouldn't use reverse method"

    is_used_build_slice = any(i.opname == 'BUILD_SLICE' for i in dis.get_instructions(reverse_inplace))
    assert not is_used_build_slice, "You should use iteration ONLY, not slicing"

    assert given_a == t.result
