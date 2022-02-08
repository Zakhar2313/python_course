import typing as tp


def revert(dct: tp.Mapping[str, str]) -> tp.Dict[str, tp.List[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """