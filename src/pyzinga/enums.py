from enum import Enum


class Color(Enum):
    White = 1
    Black = 2


class GameStateEnum(Enum):
    NotStarted = 1
    InProgress = 2
    Draw = 3
    WhiteWins = 4
    BlackWins = 5

