import inspect
from importlib.metadata import version
from pyzinga import __version__

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
                pass
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