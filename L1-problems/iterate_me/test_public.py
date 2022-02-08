import copy
import typing as tp

from .iterate_me import get_squares, get_indices_from_one, get_max_element_index, \
    get_every_second_element, get_first_three_index, get_last_three_index


def test_get_squares() -> None:
    a = [-2, 0, 5, 2, 3, 4, 3]
    a_copy = copy.deepcopy(a)
    assert get_squares(a_copy) == [4, 0, 25, 4, 9, 16, 9]
    assert a_copy == a, "You shouldn't change inputs"


def test_get_squares_empty_list() -> None:
    a: tp.List[tp.Any] = []
    a_copy = copy.deepcopy(a)
    assert get_squares(a_copy) == []
    assert a_copy == a, "You shouldn't change inputs"


def test_get_indices() -> None:
    a = [-2, 0, 5, 2, 3, 4, 3]
    a_copy = copy.deepcopy(a)
    assert get_indices_from_one(a_copy) == [1, 2, 3, 4, 5, 6, 7]
    assert a_copy == a, "You shouldn't change inputs"


def test_get_indices_empty_list() -> None:
    a: tp.List[tp.Any] = []
    a_copy = copy.deepcopy(a)
    assert get_indices_from_one(a_copy) == []
    assert a_copy == a, "You shouldn't change inputs"


def test_get_max_element_index() -> None:
    a = [-2, 0, 5, 2, 3, 4, 3]
    a_copy = copy.deepcopy(a)
    assert get_max_element_index(a_copy) == 2
    assert a_copy == a, "You shouldn't change inputs"


def test_get_max_element_index_empty_list() -> None:
    a: tp.List[tp.Any] = []
    a_copy = copy.deepcopy(a)
    assert get_max_element_index(a_copy) is None
    assert a_copy == a, "You shouldn't change inputs"


def test_get_every_second_element() -> None:
    a = [-2, 0, 5, 2, 3, 4, 3]
    a_copy = copy.deepcopy(a)
    assert get_every_second_element(a_copy) == [0, 2, 4]
    assert a_copy == a, "You shouldn't change inputs"


def test_get_every_second_element_empty_input() -> None:
    a: tp.List[tp.Any] = []
    a_copy = copy.deepcopy(a)
    assert get_every_second_element(a_copy) == []
    assert a_copy == a, "You shouldn't change inputs"


def test_get_every_second_element_one_element() -> None:
    a = [1]
    a_copy = copy.deepcopy(a)
    assert get_every_second_element(a_copy) == []
    assert a_copy == a, "You shouldn't change inputs"


def test_get_first_three_index() -> None:
    a = [-2, 0, 5, 2, 3, 4, 3]
    a_copy = copy.deepcopy(a)
    assert get_first_three_index(a_copy) == 4
    assert a_copy == a, "You shouldn't change inputs"


def test_get_first_three_index_empty_input() -> None:
    a: tp.List[tp.Any] = []
    a_copy = copy.deepcopy(a)
    assert get_first_three_index(a_copy) is None
    assert a_copy == a, "You shouldn't change inputs"


def test_get_first_three_index_without_three() -> None:
    a = [-2, 0, 5, 2]
    a_copy = copy.deepcopy(a)
    assert get_first_three_index(a_copy) is None
    assert a_copy == a, "You shouldn't change inputs"


def test_get_last_three_index() -> None:
    a = [-2, 0, 5, 2, 3, 4, 3]
    a_copy = copy.deepcopy(a)
    assert get_last_three_index(a_copy) == 6
    assert a_copy == a, "You shouldn't change inputs"


def test_get_last_three_index_empty_input() -> None:
    a: tp.List[tp.Any] = []
    a_copy = copy.deepcopy(a)
    assert get_last_three_index(a_copy) is None
    assert a_copy == a, "You shouldn't change inputs"


def test_get_last_three_index_without_three() -> None:
    a = [-2, 0, 5, 2]
    a_copy = copy.deepcopy(a)
    assert get_last_three_index(a_copy) is None
    assert a_copy == a, "You shouldn't change inputs"


def test_get_last_three_index_on_first_position() -> None:
    a = [3, 0, 5, 2, 1, 4, 6]
    a_copy = copy.deepcopy(a)
    assert get_last_three_index(a_copy) == 0
    assert a_copy == a, "You shouldn't change inputs"
