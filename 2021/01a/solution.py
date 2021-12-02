from typing import Tuple
from typing import List


def load_entry(file_path: str) -> List[int]:
    with open(file_path) as file:
        return [int(x.strip()) for x in file.readlines()]


def check_depth(previous: int, current: int, increment: int) -> Tuple[int, int]:
    print('{} ({})'.format(current, current > previous))

    if current > previous:
        increment += 1
    previous = current

    return previous, increment


if __name__ == '__main__':
    measurement = 0
    count = 0
    entries = load_entry('input.txt')
    print('{} ({})'.format(entries[0], entries[0] > measurement))
    measurement = entries[0]
    entries.pop(0)

    for entry in entries:
        measurement, count = check_depth(measurement, entry, count)

    print(count)
