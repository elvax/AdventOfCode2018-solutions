from collections import Counter

with open('data/day02.txt', 'r') as file:
    data = file.read()

def part1(data):
    twos = 0
    threes = 0
    for entry in data.split():
        counter = Counter(entry)
        if 3 in counter.values():
            threes += 1
        if 2 in counter.values():
            twos += 1

    return twos * threes
