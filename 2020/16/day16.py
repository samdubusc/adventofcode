import sys
import re

from utils.input_file import file_path_from_args
from utils.read_lines import read_lines

FIELDS_AND_VALUES = []


def valid_values(f_and_v: list) -> []:
    foo = {}
    for fv in f_and_v:
        for v in fv["values"]:
            foo[v] = 1
    return list(foo.keys())


def valid_tickets(ticket: []) -> []:
    nearby = []
    for t in ticket:
        is_valid = True
        for n in t:
            if n not in valid_values(FIELDS_AND_VALUES):
                is_valid = False
                break
        if is_valid:
            nearby.append(t)
    return nearby


def order_fields(all_tickets: []) -> []:
    nearby_tickets = valid_tickets(all_tickets)

    ordered_fields = {}
    while FIELDS_AND_VALUES:
        for i in range(len(nearby_tickets[0])):
            fields = []
            for j in range(len(nearby_tickets)):
                f = []
                for fv in FIELDS_AND_VALUES:
                    if nearby_tickets[j][i] in fv["values"]:
                        f.append(fv["field"])
                fields = f if not fields else list(set(fields) & set(f))

            if len(fields) == 1:
                for fv in FIELDS_AND_VALUES:
                    if fv['field'] == fields[0] and i not in ordered_fields:
                        ordered_fields[i] = fields[0]
                        FIELDS_AND_VALUES.remove(fv)
    return ordered_fields


def main(input_file: str) -> int:
    field_values_re = re.compile(r"^(.+): (\d+)-(\d+) or (\d+)-(\d+)$")
    values_re = re.compile(r"^(\d+,*)+$")
    nearby_re = re.compile("^nearby tickets:$")
    departure_re = re.compile("departure.*")
    is_your_ticket = True
    product = 1
    your_ticket = []
    all_tickets = []

    for line in read_lines(input_file):
        if line == "":
            continue
        else:
            if r := field_values_re.match(line):
                v = []
                for i in range(int(r.group(2)), int(r.group(3))+1):
                    v.append(i)
                for i in range(int(r.group(4)), int(r.group(5))+1):
                    v.append(i)
                FIELDS_AND_VALUES.append({"field": r.group(1), "values": v})

            if nearby_re.match(line):
                is_your_ticket = False

            if values_re.match(line):
                if is_your_ticket:
                    your_ticket = [int(n) for n in line.split(",")]
                else:
                    all_tickets.append([int(n) for n in line.split(",")])

    fields = order_fields(all_tickets)

    for i in range(len(fields)):
        if i in fields and departure_re.match(fields[i]):
            product *= your_ticket[i]

    print(product)

    return 0


if __name__ == "__main__":
    sys.exit(main(file_path_from_args()))
