import typing as tp
from typing_extensions import Protocol


class Gettable(Protocol):
    def __getitem__(self, item: int) -> tp.Union[str, bool]:
        pass

    def __len__(self) -> int:
        pass


def get(container: Gettable, index: int) -> tp.Optional[tp.Union[str, bool]]:
    if container:
        return container[index]

    return None
