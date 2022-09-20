from dataclasses import dataclass

from pyzinga.enums import GameStateEnum


@dataclass
class GameState:
    state: GameStateEnum = GameStateEnum.NotStarted

    @classmethod
    def from_string(cls, state_string: str):
        return GameState(state=GameStateEnum[state_string])

    @classmethod
    def is_valid(cls, state_string: str):
        return state_string in [e.name for e in GameStateEnum]

    def __str__(self):
        return self.state.name
