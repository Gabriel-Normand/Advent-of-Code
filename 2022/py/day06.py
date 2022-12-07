def part1(line):
    length = 4
    for i in range(length, len(line)):
        signal = line[i-length:i]
        # sets must be all unique items so if it's the right length, it is correct.
        if len(set(signal)) == length:
            return i


def part2(line):
    length = 14
    for i in range(length, len(line)):
        signal = line[i-length:i]
        if len(set(signal)) == length:
            return i


data = open("inputs/day06.txt").read().strip()
print(part1(data))
print(part2(data))
