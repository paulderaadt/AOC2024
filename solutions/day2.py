from utils.filereaders import Linereader


def is_sorted(entry):
    return sorted(entry) == entry or sorted(entry, reverse=True) == entry


def is_num_safe(entry):
    safe = True
    for first, second in zip(entry, entry[1:]):
        safe &= 0 < abs(first - second) < 4
    return safe


def part1(data):
    safecounts = 0
    for line in data:
        safe = is_sorted(line)
        if not safe:
            continue
        else:
            safe &= is_num_safe(line)
        if safe:
            safecounts += 1
    return safecounts


def part2(data):
    safecounts = 0
    for line in data:
        safes = []
        for i in range(0, len(line)):
            one_removed_line = line[:i] + line[i + 1:]
            safe = is_sorted(one_removed_line)
            if not safe:
                continue
            safe &= is_num_safe(one_removed_line)
            safes += [safe]
        if any(safes):
            safecounts += 1
    return safecounts


def main():
    data = Linereader('../inputs/day2.txt').parse()
    data = [[int(num) for num in item.split()] for item in data]
    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    main()

