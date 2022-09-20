from game_type import GameType
from pyzinga.game_string import GameString


class Board:
    def __init__(self, game_string: GameString | str = None):
        self.game_string = game_string if isinstance(game_string, GameString) else GameString(game_string)

    @classmethod
    def from_game_type_string(cls, game_type_string):
        return Board(game_string=GameString(type=game_type_string))

    @classmethod
    def from_game_string(cls, game_string):
        return Board(game_string=game_string)

    def __str__(self):
        return self.game_string


