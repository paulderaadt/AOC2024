from dataclasses import dataclass
from utils.filereaders import Flatreader

@dataclass
class Rule:
    before: int
    after: int


def parse(data):
    rule, pages = data.split('\n\n')
    rule = rule.split('\n')
    rule = [rules.split('|') for rules in rule]
    toint = lambda a: (int(a[0]), int(a[1]))
    rule = list(map(toint, rule))
    rule = [Rule(before=item[0], after=item[1]) for item in rule]
    pages = pages.split('\n')
    pages = [page.split(",") for page in pages]
    pages = [list(map(int, page)) for page in pages]
    return rule, pages

def prepare_rules(rules):
    rulemap = {}
    for rule in rules:
        if rule.before not in rulemap:
            rulemap[rule.before] = [rule.after]
        else:
            rulemap[rule.before] += [rule.after]
    return rulemap

def check_page(rulemap, line):
    for i, page in enumerate(line):
        must_precede = rulemap.get(page, [])
        preceding = line[:i]
        #print(f'{page} must precede {must_precede} and is preceded by
        # {preceding}')
        overlap = set(preceding) & set(must_precede)
        #print(f'overlap: {overlap}')
        if overlap:
            return False
    return True


def part1(pages, rulemap):
    passes = []
    for line in pages:
        page_passes = check_page(rulemap, line)
        if page_passes:
            passes.append(line[len(line) // 2])
    print(sum(passes))

def part2(pages, rulemap):
    fails = []
    for line in pages:
        page_passes = check_page(rulemap, line)
        if not page_passes:
            fails.append(line)
    fixed = []

    # bubble sort the fails with the rulemap dictating wether a swap happens
    for line in fails:
        n = len(line)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if line[j] in rulemap[line[j + 1]]:
                    line[j], line[j + 1] = line[j + 1], line[j]
        fixed.append(line[len(line) // 2])
    print(sum(fixed))



def main():
    data = Flatreader('../inputs/day5.txt').parse()
    rules, pages = parse(data)
    rulemap = prepare_rules(rules)
    #part1(pages, rulemap)
    part2(pages, rulemap)



if __name__ == '__main__':
    main()