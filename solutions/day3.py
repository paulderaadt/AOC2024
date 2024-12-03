from utils.filereaders import Flatreader
from re import findall, finditer

def extract_mul(mul):
    match = findall(r'\d{1,3}', mul)
    match = list(map(int, match))
    return match


def part1(data):
    muls = findall(r'mul\(\d{1,3},\d{1,3}\)', data)
    mulpairs = []
    for mul in muls:
        mulpairs.append(extract_mul(mul))
    print(sum([a * b for a, b in mulpairs]))
    return mulpairs


def part2(data):
    muls = finditer(r"(mul\(\d{1,3},\d{1,3}\)|(do\(\))|(don't\(\)))", data)
    do = True
    multotal = 0
    for mul in muls:
        if mul.group(0)[0:3] == 'mul':
            mul = extract_mul(mul.group(0))
            if do:
                a, b = mul
                multotal += a * b
        elif mul.group(0)[0:3] == 'do(':
            do = True
        elif mul.group(0)[0:3] == 'don':
            do = False

    print(multotal)
def main():
    data = Flatreader('../inputs/day3.txt').parse()
    data = data.replace('\n', '')
    part1(data)
    part2(data)


main()