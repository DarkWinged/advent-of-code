import argparse
from typing import Tuple
from typing import List
from typing import Dict


def load_entry(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path) as file:
        return [x.strip() for x in file.readlines()]


def char_to_bool(character):
    if character == '1':
        return True
    else:
        return False


def map_entries(entries):
    return list(map(lambda x: list(map(char_to_bool, x)), entries))


def list_to_str(bool_list):
    result = ''
    for boolean in bool_list:
        if boolean:
            result = '{}{}'.format(result, '1')
        else:
            result = '{}{}'.format(result, '0')
    return result


def o2_bit_criteria(bits):
    common_value = list(filter(bool, bits))
    if len(common_value) >= len(bits)/2:
        return True
    else:
        if len(common_value) == len(bits)/2:
            return True
        else:
            return False


def co2_bit_criteria(bits):
    common_value = list(filter(bool, bits))
    if len(common_value) >= len(bits) / 2:
        return False
    else:
        if len(common_value) == len(bits) / 2:
            return False
        else:
            return True


def calculate_o2_rate(entries):
    index = 0
    result = entries
    while len(result) > 1 and index < len(entries[0]):
        common = o2_bit_criteria(list(map(lambda x: x[index], result)))
        result = list(filter(lambda x: x[index] == common, result))
        index += 1
    return list_to_str(result[0])


def calculate_co2_rate(entries):
    index = 0
    result = entries
    while len(result) > 1 and index < len(entries[0]):
        common = co2_bit_criteria(list(map(lambda x: x[index], result)))
        result = list(filter(lambda x: x[index] == common, result))
        index += 1
    return list_to_str(result[0])


def calculate_life_support(entries):
    entry_map = map_entries(entries)
    o2_rate = int(calculate_o2_rate(entry_map), 2)
    co2_rate = int(calculate_co2_rate(entry_map), 2)
    return o2_rate * co2_rate


def run_test():
    entries = load_entry('sample.txt')

    with open('sample_result.txt') as file:
        answer = int(file.read().strip())

    result = calculate_life_support(entries)
    print('test result =', result)

    return result == answer


def run_solution():
    entries = load_entry('input.txt')
    return calculate_life_support(entries)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Day 3 part 1 solution")
    parser.add_argument('--T', dest='test', default=True, type=bool, help='enables test mode')

    args = parser.parse_args()

    if args.test:
        print(run_test())
    else:
        print(run_solution())
