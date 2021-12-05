import argparse
from typing import Tuple
from typing import List
from typing import Dict


def load_entry(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path) as file:
        return [x.strip() for x in file.readlines()]


def run_test():
    entries = load_entry('sample.txt')
    result = play_bigno(entries)

    with open('sample_result.txt') as file:
        answer = int(file.read().strip())

    print('test result =', result)

    return result == answer


def run_solution():
    entries = load_entry('input.txt')
    result = play_bigno(entries)
    return result


def loop_and_filter(collection: List[int], source: str, filter: str) -> List[int]:
    for x in source:
        if x != filter:
            collection[-1] = collection[-1]*10 + int(x)
        else:
            collection.append(0)
    return collection[0:-1]


def init_draws(entries: list[str]) -> Tuple[List[int], List[str]]:
    return loop_and_filter([0], entries[0], ','), entries[2:]


def init_boards(entries: List[str]) -> List[List[List[int]]]:
    filtered_entries = list(filter(lambda x: x != '', entries))
    board_count = int(len(filtered_entries)/5)
    return[[[int(x) for x in filtered_entries[(y+(5*z))].split()] for y in range(5)] for z in range(board_count)]


def init_truthy_boards(boards: List[List[List[int]]]) -> List[List[List[bool]]]:
    return [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]


def init_bingo(entries) -> Tuple[List[int], List[List[List[int]]], List[List[List[bool]]]]:
    draws, entries = init_draws(entries)
    boards = init_boards(entries)
    truthy_boards = init_truthy_boards(boards)

    return draws, boards, truthy_boards


def play_bigno(entries):
    draws, boards, truthy_boards = init_bingo(entries)
    print(draws, boards, truthy_boards)

    for draw in draws:
        print('drawing', draw)
        won, score, truthy_boards = update_boards(draw, boards, truthy_boards)
        if won:
            return score

    return truthy_boards


def update_boards(draw: int, boards: List[List[List[int]]], truthy_boards: List[List[List[bool]]]) -> Tuple[bool, int, List[List[List[bool]]]]:
    print('boards length', len(boards))
    for z in range(len(boards)):
        x, y, truthy_boards[z] = update_board(draw, boards[z], truthy_boards[z])
        if x is not None and y is not None:
            print(z, y, x)
            if check_win(truthy_boards[z], y, x):
                score = score_board(truthy_boards[z], boards[z], boards[z][y][x])
                return True, score, truthy_boards

    return False, 0, truthy_boards


def update_board(draw: int, board: List[List[int]], truthy_board: List[List[bool]]) -> Tuple[int, int, List[List[bool]]]:
    Y = None
    X = None

    for y, row in enumerate(board):
        for x, entry in enumerate(row):
            if entry == draw:
                truthy_board[y][x] = True
                print_board(board)
                return x, y, truthy_board

    return X, Y, truthy_board


def score_board(truthy_board: List[List[bool]], board: List[List[bool]], last_draw: int) -> int:
    print_board(truthy_board)
    print(sum([board[y][x] for x in range(5) for y in range(5) if not truthy_board[y][x]]), last_draw)
    result = sum([board[y][x] for x in range(5) for y in range(5) if not truthy_board[y][x]]) * last_draw
    return result


def check_win(board: List[List[bool]], y: int, x: int) -> bool:
    return all([board[y][X] for X in range(5)]) or all([board[Y][x] for Y in range(5)])


def print_board(board: List[List[bool]]):
    for y in board:
        print(y)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Day 3 part 1 solution")
    parser.add_argument('--T', dest='test', default=False, type=bool, help='enables test mode')

    args = parser.parse_args()

    if args.test:
        print(run_test())
    else:
        print(run_solution())
