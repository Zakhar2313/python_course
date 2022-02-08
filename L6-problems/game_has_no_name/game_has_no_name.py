import typing as tp


class Player:
    def __init__(self) -> None:
        self.game_m = "start"
        self.my_m = "ready"
        self.to_delete_m: tp.Union[str, None] = None

    def ready(self, next_game_method: str, next_my_method: str) -> None:
        """
        :param next_game_method: next game class method to call
        :param next_my_method: next method game will call
        """


    def play(self, game: tp.Any) -> None:
        """
        :param game: some class with method start
        """
