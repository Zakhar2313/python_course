import pytest


# Don't change this function!
# This function specially written with bugs for checking by `test_check_ctr`
def ctr(clicks: int, shows: int) -> float:
    """
    Calculate ctr
    :param clicks: number of clicks on banner
    :param shows: number of banners shows
    :return: clicks-through rate.
             If there are no shows, return 0.0
             If clicks greater then shows, return 1
    """

@pytest.mark.skip
def test_check_ctr(clicks: int, shows: int, expected_result: float) -> None:
    """
    Write simple test for defined above function ```ctr```
        which takes function parameters and expected result and assert if something goes wrong with
        "Wrong ctr calculation" message
    :param clicks: parameter for  ctr function
    :param shows: parameter for  ctr function
    :param expected_result: result to compare with
    :return: None
    """


# This is your correct implementation
def ctr2(clicks: int, shows: int) -> float:
    """
    Calculate ctr. Presumed that clicks always less or equals to shows
    :param clicks: number of clicks on banner
    :param shows: number of banners shows
    :return: clicks-through rate.
             If there are no shows, return 0.0
    """
