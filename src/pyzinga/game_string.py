from dataclasses import dataclass

from pyzinga.game_state import GameState
from pyzinga.game_turn import GameTurn
from pyzinga.game_type import GameType


@dataclass
class GameString:
    type: GameType | str = None
    state: GameState | str = None
    turn: GameTurn | str = None

    @classmethod
    def is_valid(cls, gs: str) -> bool:
        pass

    def __str__(self):
        f"{self.type};{self.state};{self.state}"