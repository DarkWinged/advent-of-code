def load_entry(file_path=None):
    lines = []
    with open(file_path) as file:
        for line in file.readlines():
            lines.append(line)
    return lines


def check_depth(m, c, r):
    print('{} > {} is {}'.format(r, m, r > m))

    if r > m:
        c += 1
    m = r

    return m, c


if __name__ == '__main__':
    measurement = 0
    count = 0
    entries = load_entry('input.txt')
    measurement = int(entries[0])
    entries.pop(0)

    for entry in entries:
        result = check_depth(measurement, count, int(entry))
        measurement = result[0]
        count = result[1]

    print(measurement)
    print(count)
