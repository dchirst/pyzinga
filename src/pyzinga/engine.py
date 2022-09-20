
from pyzinga import __version__
from pyzinga import Board
from pyzinga.game_string import GameString
from pyzinga.game_type import GameType


class Engine:
    def __init__(self):
        pass

    def __repr__(self):
        return f"id {__name__} v{__version__}"


    def info(self):
        return self.__repr__()


    def output_command(self, txt: str):
        print(txt)
        print("ok")

    def parse_command(self, cmd: str) -> bool:
        """
        Takes a text command from UHP and implements command
        :param cmd: command as defined by Universal Hive Protocal
        :type cmd: str
        :return: whether the command executed sucessfully
        :rtype: bool
        """
        split_cmd = cmd.split()
        match split_cmd[0]:
            case "info":
                self.output_command(self.info())
            case "newgame":
                if len(split_cmd) == 2:
                    new_game_params = split_cmd[1]
                    if GameType.is_valid(new_game_params):
                        board = Board.from_game_type_string(new_game_params)
                    elif GameString.is_valid(new_game_params):
                        board = Board.from_game_string(new_game_params)
                else:
                    board = Board()

                self.board = board
                self.output_command(self.board)
            case "play":
                pass
            case "pass":
                pass
            case "validmoves":
                pass
            case "bestmove":
                pass
            case "undo":
                pass
            case "options":
                pass
            case "exit":
                exit()
            case _:
                return False