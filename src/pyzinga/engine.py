import inspect
from importlib.metadata import version


class Engine:
    def __init__(self):
        pass

    def __repr__(self):
        s = inspect.stack()
        return f"id {__name__} v{version('pyzinga')}"

    def info(self):
        return self.__repr__()

    def output_command(self, txt: str):
        print(txt)
        print("ok")