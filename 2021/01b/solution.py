def load_entry(file_path=None):
    lines = []
    with open(file_path) as file:
        for line in file.readlines():
            lines.append(line)
    return lines


def check_depth(p, c, i):
    print('{} ({})'.format(c, c > p))

    if c > p:
        i += 1
    p = c

    return p, i


if __name__ == '__main__':
    measurement = 0
    count = 0
    entries = load_entry('input.txt')
    measurement = int(entries[0]) + int(entries[1]) + int(entries[2])

    print('{} ({})'.format(measurement, 'N/A'))
    entries.pop(0)

    for entry in entries:
        entry_index = entries.index(entry)
        if entry_index + 2 < len(entries):
            window = int(entry) + int(entries[entry_index+1]) + int(entries[entry_index+2])
            result = check_depth(measurement, window, count)
            measurement = result[0]
            count = result[1]
        else:
            break

    print(count)
