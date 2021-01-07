import sys

from utils.input_file import file_path_from_args
from utils.read_lines import read_lines


def main(input_file: str) -> int:
    foo = []

    for line in read_lines(input_file):
        foo.append(line)

    print(foo)

    return 0


if __name__ == "__main__":
    sys.exit(main(file_path_from_args()))
