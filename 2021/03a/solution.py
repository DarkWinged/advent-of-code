import argparse
from typing import Tuple
from typing import List
from typing import Dict


def load_entry(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path) as file:
        return [x.strip() for x in file.readlines()]


def transpose_entries(entries):
    entry_transpose = {}
    i = 0
    while i < len(entries[0]):
        entry_transpose[i] = []
        i += 1

    for entry in entries:
        for index, character in enumerate(entry):
            if character == '1':
                entry_transpose[index].append(True)
            else:
                entry_transpose[index].append(False)
    return entry_transpose


def list_to_str(bool_list):
    result = ''
    for boolean in bool_list:
        if boolean:
            result = '{}{}'.format(result, '1')
        else:
            result = '{}{}'.format(result, '0')
    return result


def calculate_gamma_rate(entry_transpose):
    bools = list(map(lambda x: len(list(filter(bool, entry_transpose[x]))) > len(entry_transpose[x])/2, entry_transpose))
    return list_to_str(bools)


def calculate_epsilon_rate(entry_transpose):
    bools = list(map(lambda x: len(list(filter(bool, entry_transpose[x]))) < len(entry_transpose[x])/2, entry_transpose))
    return list_to_str(bools)


def calculate_power_consumption(entries):
    entry_transpose = transpose_entries(entries)
    gamma = int(calculate_gamma_rate(entry_transpose), 2)
    epsilon = int(calculate_epsilon_rate(entry_transpose), 2)
    return gamma * epsilon


def run_test():
    entries = load_entry('sample.txt')

    with open('sample_result.txt') as file:
        answer = int(file.read().strip())

    result = calculate_power_consumption(entries)
    print(result)

    return result == answer


def run_solution():
    entries = load_entry('input.txt')
    return calculate_power_consumption(entries)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Day 3 part 1 solution")
    parser.add_argument('--T', dest='test', default=False, type=bool, help='enables test mode')

    args = parser.parse_args()

    if args.test:
        print(run_test())
    else:
        print(run_solution())
