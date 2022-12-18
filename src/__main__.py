"""Call cli with `python -m gitxl ...`"""
import sys
from .cli import CommandParser

def main():
    command_parser = CommandParser(sys.argv[1:])
    command_parser.execute()

if __name__ == "__main__":
    main()
