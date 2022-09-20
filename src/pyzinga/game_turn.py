from dataclasses import dataclass
from enums import Color


class GameTurn:
    color: Color = Color.White
    turn: int = 1

    def __str__(self):
        return f"{self.color.name}[{self.turn}]"

    def increment(self):
        if self.color == Color.White:
            self.color = Color.Black
        elif self.color == Color.Black:
            self.color = Color.White
            self.turn += 1
        else:
            raise Exception("GameType attribute 'color' has a value of neither WHITE nor BLACK. Something is going wrong"
                            "here.")
