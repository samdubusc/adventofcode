import sys
import re
import copy

from utils.input_file import file_path_from_args
from utils.read_lines import read_lines


def version_1(program: []):
    mem = {}
    mask = ""
    total = 0
    for line in program:
        if (mask_re := re.compile('^mask = (\w+)$').match(line)):
            mask = mask_re.group(1)

        if (mem_re := re.compile('^mem\[(\d+)\] = (\w+)$').match(line)):
            address = mem_re.group(1)
            value = mem_re.group(2)

            value = list(format(int(value), '036b'))

            for i, b in enumerate(list(mask[::-1]), start=1):
                if b != 'X':
                    value[-i] = b

            mem[address] = int("".join(value), 2)

    for v in mem.values():
        total += int(v)

    print(f"v1.0 total: {total}")


def version_2(program: []):
    mem = {}
    mask = ""
    total = 0
    for line in program:
        addresses = []
        if (mask_re := re.compile('^mask = (\w+)$').match(line)):
            mask = mask_re.group(1)

        if (mem_re := re.compile('^mem\[(\d+)\] = (\w+)$').match(line)):
            address = mem_re.group(1)
            value = int(mem_re.group(2))

            address = list(format(int(address), '036b'))

            for i, b in enumerate(list(mask[::-1]), start=1):
                if b != '0':
                    address[-i] = b

            addresses.append(0)
            for i, b in enumerate(address[::-1], start=0):
                if b == '0':
                    continue
                if b == 'X':
                    foo = copy.deepcopy(addresses)
                    for j in range(len(addresses)):
                        addresses[j] += (2 ** i)
                    addresses.extend(foo)
                else:
                    for j in range(len(addresses)):
                        plus = int(b) * (2 ** i)
                        addresses[j] += plus

            for a in addresses:
                mem[a] = value

    for v in mem.values():
        total += v

    print(f"v2.0 total: {total}")


def main(input_file: str) -> int:
    program = []
    for line in read_lines(input_file):
        if line == "":
            break
        program.append(line)

    version_1(program)
    version_2(program)
    return 0


if __name__ == "__main__":
    sys.exit(main(file_path_from_args()))
