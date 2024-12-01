from collections import Counter

def read_input():
    with open('../inputs/day1.txt', 'r') as f:
        left = []
        right = []

        for line in f:
            templeft, tempright = line.split()
            left += [int(templeft)]
            right += [int(tempright)]
    return left, right


def part1():
    left, right = read_input()
    left.sort()
    right.sort()
    diffs = 0
    for l, r in zip(left, right):
        diffs += abs(l - r)
    print(diffs)


def part2():
    left, right = read_input()
    rightcounts = Counter(right)
    similarity_score = 0

    for num in left:
        if num in rightcounts:
            similarity_score += num * rightcounts.get(num)
    print(similarity_score)


if __name__ == '__main__':
    part1()
    part2()