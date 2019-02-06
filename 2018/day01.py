with open('data/day01.txt', 'r') as file:
    data = file.read()


def part1(data):
    return sum( map(int, data.split()) )

def part2(data):
    seen = set()
    freq = 0
    data = data.split()
    while True:
        for val in data:
            freq += int(val)
            if freq in seen:
                return freq
            seen.add(freq)