import pytest

from .make_assert import test_check_ctr, ctr2


def test_clicks_equals_shows_not_assert() -> None:
    test_check_ctr(2, 2, 1.0)


def test_zero_shows_not_assert() -> None:
    test_check_ctr(100, 0, 0.0)


def test_zero_clicks_not_assert() -> None:
    test_check_ctr(100, 0, 0.0)


def test_fractional_ctr_assert() -> None:
    with pytest.raises(AssertionError, match="Wrong ctr calculation"):
        test_check_ctr(1, 2, 0.5)


def test_ctr_greater_then_one_assert() -> None:
    with pytest.raises(AssertionError, match="Wrong ctr calculation"):
        test_check_ctr(10, 5, 1.0)


def test_ctr2_clicks_equals_shows() -> None:
    result = ctr2(2, 2)
    assert type(result) == float
    assert result == 1.0


def test_ctr2_zero_shows() -> None:
    result = ctr2(0, 0)
    assert type(result) == float
    assert result == 0.0


def test_ctr2_fractional() -> None:
    result = ctr2(1, 2)
    assert type(result) == float
    assert result == 0.5


def test_ctr2_clicks_greater_than_shows() -> None:
    with pytest.raises(AssertionError, match="Clicks greater than shows"):
        ctr2(2, 1)
