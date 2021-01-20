import sys

from utils.input_file import file_path_from_args
from utils.read_lines import read_lines

NUMBER_OF_TURNS = 30000000


def main(input_file: str) -> int:
    turns = []
    last = {}

    numbers = [int(n) for n in list(read_lines(input_file))[0].split(",")]

    for turn in range(NUMBER_OF_TURNS):
        if turn < len(numbers):
            turns.append(numbers[turn])
        else:
            turns.append(turn - last[turns[turn - 1]] if turns[-1] in last else 0)
        last[turns[turn-1]] = turn

    print(turns[-1])

    return 0


if __name__ == "__main__":
    sys.exit(main(file_path_from_args()))
