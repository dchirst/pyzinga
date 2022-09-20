from dataclasses import dataclass

@dataclass
class GameType:
    ladybug: bool = False
    mosquito: bool = False
    pillbug: bool = False

    def __str__(self):
        expansion_str = ""
        if self.mosquito:
            expansion_str += "M"
        if self.ladybug:
            expansion_str += "L"
        if self.pillbug:
            expansion_str += "P"
        return "Base" + f"+{expansion_str}" if expansion_str else ""
