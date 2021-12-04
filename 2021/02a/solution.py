from typing import Tuple
from typing import List
from typing import Dict


def load_entry(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path) as file:
        return [(x.strip()[0:-2], int(x.strip()[-1])) for x in file.readlines()]


def sum_direction(entries: List[Tuple[str, int]], collection: Dict[str, int] = {}):
    for x in entries:
        collection[x[0]] += x[1]
    return collection


if __name__ == '__main__':
    entries = load_entry('input.txt')
    direction = {'forward': 0, 'down': 0, 'up': 0}
    result = sum_direction(entries, direction)
    print(result)
    print('x:{}, y:{}'.format(result['forward'], result['down']-result['up']))
    print(result['forward']*(result['down']-result['up']))
