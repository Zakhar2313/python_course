import copy
import dis
import dataclasses
import itertools

import typing as tp

import pytest


from .bin_tricky import find_median


@dataclasses.dataclass
class Case:
    nums1: tp.List[int]
    nums2: tp.List[int]

    def __str__(self) -> str:
        return 'find_median_in_{}_and_{}'.format(self.nums1, self.nums2)


BIG_VALUE = 10**5


def get_range_with_peak_on_position(range_size: int, position: int) -> tp.List[int]:
    if position >= range_size or position < 0:
        raise ValueError("Position should be in [0, range_size)")

    return list(itertools.chain(range(position), [range_size + 1], range(range_size - position - 1, position, -1)))


TEST_CASES = [
    Case(nums1=[1], nums2=[2]),
    Case(nums1=[], nums2=[2]),
    Case(nums1=[1], nums2=[]),
    Case(nums1=[1, 2], nums2=[]),
    Case(nums1=[1, 2, 3], nums2=[]),
    Case(nums1=[1, 2, 3, 5], nums2=[]),
    Case(nums1=[1, 2, 3, 5, 7], nums2=[]),
    Case(nums1=[], nums2=[1, 2]),
    Case(nums1=[], nums2=[1, 2, 3]),
    Case(nums1=[], nums2=[1, 2, 3, 5]),
    Case(nums1=[], nums2=[1, 2, 3, 5, 7]),
    Case(nums1=[], nums2=[1, 2, 3, 5, 7]),
    Case(nums1=[-1, -1, -1], nums2=[-1, -1, -1]),
    Case(nums1=[1, 2],  nums2=[1, 2]),
    Case(nums1=[1, 1], nums2=[1, 1]),
    Case(nums1=[1, 3], nums2=[2]),
    Case(nums1=[1, 2, 3, 4], nums2=[3, 4, 5, 6]),
    Case(nums1=[1, 2, 3, 4], nums2=[1, 2, 3, 4]),
    Case(nums1=[1, 3, 5, 7], nums2=[2, 4, 6, 8]),
    Case(nums1=[1, 3, 5, 7], nums2=[-1, 2, 4, 6, 8]),
    Case(nums1=[1, 3, 5, 7], nums2=[-1, -1, -1]),
    Case(nums1=[-1, 5, 8, 17], nums2=[-7, 15, 20]),
    Case(nums1=[-1, 5, 8, 17], nums2=[21, 25, 38]),
    Case(nums1=[1, 3, 5, 7], nums2=[-5, -4, 0]),
    Case(nums1=[1, 2], nums2=[3]),
    Case(nums1=[1], nums2=[2, 3]),
    Case(nums1=[1, 2], nums2=[3, 4]),
    Case(nums1=[3, 4], nums2=[1, 2]),
    Case(nums1=[3, 4, 5], nums2=[1]),
    Case(nums1=[1], nums2=[3, 4, 5]),
    Case(nums1=[3, 4, 5, 6, 7, 8], nums2=[1, 2]),
]


def dummy_implementation(nums1: tp.List[int], nums2: tp.List[int]) -> float:
    combined_nums = sorted(nums1 + nums2)
    m = len(nums1)
    n = len(nums2)
    return (combined_nums[(m + n) // 2] + combined_nums[(m + n - 1) // 2]) / 2


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_find_value(t: Case) -> None:
    nums1_copy = copy.deepcopy(t.nums1)
    nums2_copy = copy.deepcopy(t.nums2)

    answer = find_median(nums1_copy, nums2_copy)

    assert t.nums1 == nums1_copy, "You shouldn't change inputs"
    assert t.nums2 == nums2_copy, "You shouldn't change inputs"
    assert type(answer) == float, "You shouldn't return different types from the same function"

    is_used_sorted = any(i.argval == 'sorted' for i in dis.get_instructions(find_median))
    assert not is_used_sorted, "You should use iteration ONLY, not manually sorting"

    assert answer == dummy_implementation(t.nums1, t.nums2)
