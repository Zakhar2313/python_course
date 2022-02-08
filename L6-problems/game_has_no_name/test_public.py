from importlib import reload
import pytest
import typing as tp

from . import game_has_no_name


@pytest.fixture()
def player_class() -> tp.Generator[tp.Type[game_has_no_name.Player], None, None]:
    reload(game_has_no_name)
    yield game_has_no_name.Player


class LooseException(Exception):
    pass


class WinException(Exception):
    def __init__(self, value: float) -> None:
        self.prise = value
        super().__init__()


class Game:
    def start(self, player: game_has_no_name.Player) -> None:
        player.ready('next_step', 'next_player_method')

    def next_step(self, player: game_has_no_name.Player) -> None:
        if hasattr(player, 'ready'):
            raise LooseException()
        player.next_player_method('another_game_step', 'yet_another_player_method')
   
    def another_game_step(self, player: game_has_no_name.Player) -> None:
        if hasattr(player, 'next_player_method'):
            raise LooseException()
        raise WinException(2)

def test_player(player_class: tp.Type[game_has_no_name.Player]) -> None:
    game = Game()
    player = player_class()

    with pytest.raises(WinException):
        for i in range(1000000):
            player.play(game)
