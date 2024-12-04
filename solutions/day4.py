from utils.filereaders import Linereader
from utils.Coordinates import CardinalDirections

def part1(data):
    find = 'XMAS'
    counts = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            for direction in CardinalDirections:
                found = ''
                try:
                    for step in range(len(find)):
                        x_direction = x + step * direction.x
                        y_direction = y + step * direction.y
                        if x_direction < 0 or y_direction < 0:
                            raise IndexError
                        found += data[y_direction][x_direction]
                    if found == find:
                        counts += 1
                except IndexError:
                    pass
    return counts

def part2(data):
    counts = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            found = ''
            for direction in CardinalDirections:
                try:
                    x_direction = x + direction.x
                    y_direction = y + direction.y
                    if x_direction < 0 or y_direction < 0:
                        raise IndexError
                    found += data[y_direction][x_direction]
                    if direction == CardinalDirections.WEST:
                        found += data[y][x]
                except IndexError:
                    pass
            if matches_crossmas(found):
                print(found, y, x, direction)
                counts += 1
    return counts


def matches_crossmas(found, search='MAS'):
    # Diagonal slice from top left to bottom right
    diagonal1 = found[::4]
    # Diagonal slice from top right to bottom left
    diagional2 = found[2:8:2]
    correct_crossmas = diagonal1 == search or diagonal1[::-1] == search
    correct_crossmas &= diagional2 == search or diagional2[::-1] == search
    return correct_crossmas



def main():
    data = Linereader('../inputs/day4.txt').parse()
    data = [list(line) for line in data]
    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    main()
