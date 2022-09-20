from pyzinga.engine import Engine

if __name__ == '__main__':
    engine = Engine()
    while True:
        command = input()
        engine.parse_command(command)

