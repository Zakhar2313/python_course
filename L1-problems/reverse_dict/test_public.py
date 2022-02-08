import copy
import dataclasses
import typing as tp

import pytest


from .reverse_dict import revert


@dataclasses.dataclass
class Case:
    dct: tp.Mapping[str, str]
    result: tp.Mapping[str, tp.List[str]]

    def __str__(self) -> str:
        return 'revert_{}'.format(self.dct)


TEST_CASES = [
    Case(dct={}, result={}),
    Case(dct={"a": "1"}, result={"1": ["a"]}),
    Case(dct={"a": "1", "b": "2"}, result={"1": ["a"], "2": ["b"]}),
    Case(dct={"a": "1", "b": "2", "c": "1"}, result={"1": ["a", "c"], "2": ["b"]}),
    Case(dct={"a": "1", "b": "2", "c": "1", "d": "1"}, result={"1": ["a", "c", "d"], "2": ["b"]}),
    Case(dct={"a": "1", "b": "2", "c": "1", "d": "1", "e": "2"}, result={"1": ["a", "c", "d"], "2": ["b", "e"]}),
    Case(dct={"a": "1", "b": "2", "c": "1", "d": "1", "e": "2", "g": "3"}, result={"1": ["a", "c", "d"],
                                                                                   "2": ["b", "e"], "3": ["g"]}),
]


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_reverse_dict(t: Case) -> None:
    given_dct = copy.deepcopy(t.dct)

    answer = revert(given_dct)

    assert t.dct == given_dct, "You shouldn't change input dict"

    for k, v in answer.items():
        v.sort()

    assert answer == t.result
    assert isinstance(answer, dict)
