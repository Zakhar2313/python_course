import typing as tp


def get_common_numerical_type(type1: type, type2: type) -> type:
    """
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [int, float, complex] types
    :param type2: one of [int, float, complex types
    :return: the most concrete common type, which can be used to convert both input values
    """
