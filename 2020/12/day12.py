import sys
import re

from utils.input_file import file_path_from_args
from utils.read_lines import read_lines


def main(input_file: str) -> int:
    instructions = []
    ship_x = 0
    ship_y = 0
    waypoint_x = 10
    waypoint_y = 1

    for line in read_lines(input_file):
        if line == "":
            break
        instructions.append(line)
        line_re = re.match('^([A-Z])(\d+)$', line)
        d = line_re.group(1)
        v = int(line_re.group(2))

        if d == 'F':
            ship_x += waypoint_x * v
            ship_y += waypoint_y * v
        if d == 'E':
            waypoint_x += v
        if d == 'W':
            waypoint_x -= v
        if d == 'N':
            waypoint_y += v
        if d == 'S':
            waypoint_y -= v

        if d == 'R':
            for i in range(0, int(v/90)):
                foo = waypoint_y
                waypoint_y = waypoint_x * -1
                waypoint_x = foo


        if d == 'L':
            for i in range(0, int(v/90)):
                foo = waypoint_x
                waypoint_x = waypoint_y * -1
                waypoint_y = foo


    print(abs(ship_x)+abs(ship_y))

    return 0


if __name__ == "__main__":
    sys.exit(main(file_path_from_args()))
