def part1(elves):
    most = 0
    for elf in elves:
        # split the elf into lines and parse as ints, sum all ints
        calories = sum(map(int, elf.split()))
        # keep the higher value
        most = max(calories, most)
    return most


def part2(elves):
    calories = []
    for elf in elves:
        # same as before but save all sums in a list
        calories.append(sum(map(int, elf.split())))
    # sort the list and return the sum of the last 3 (highest) values
    calories.sort()
    return sum(calories[-3:])


data = open("inputs/day01.txt").read().strip().split("\n\n")
print(part1(data))
print(part2(data))
