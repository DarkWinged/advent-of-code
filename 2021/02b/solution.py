from typing import Tuple
from typing import List
from typing import Dict


def load_entry(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path) as file:
        return [(x.strip()[0:-2], int(x.strip()[-1])) for x in file.readlines()]


def sum_direction(entries: List[Tuple[str, int]], collection: Dict[str, int] = {}):
    for x in entries:
        if x[0] == 'forward':
            collection[x[0]] += x[1]
            collection['depth'] += collection['aim']*x[1]
        if x[0] == 'up':
            collection['aim'] -= x[1]
        if x[0] == 'down':
            collection['aim'] += x[1]
    return collection


if __name__ == '__main__':
    entries = load_entry('input.txt')
    direction = {'forward': 0, 'depth': 0, 'aim':0}
    result = sum_direction(entries, direction)
    print(result)
    print('x:{}, y:{}, a:{}'.format(result['forward'], result['depth'], result['aim']))
    print(result['forward']*result['depth'])
