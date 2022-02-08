import typing as tp


def filter_list_by_list(a: tp.Sequence[int], b: tp.Sequence[int]) -> tp.List[int]:
    """
    Filter first sorted lists by other sorted list
    :param a: first sorted list
    :param b: second sorted list
    :return: filtered sorted list
    """
