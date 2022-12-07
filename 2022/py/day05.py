import re


def part1(file):
    # seperates the crates from the instructions by the blank line
    crates, instructions = file.split("\n\n")
    # _ is used as a throwaway value
    # creates a blank array of 9
    stacks = [[] for _ in range(9)]

    for line in crates.splitlines():
        # reads line, starts at 1, ends at end of line length, reads each 4th item
        for stackIdx, lineIdx in enumerate(range(1, len(line), 4)):
            # if it finds a value add it to the end of the corresponding stack
            if line[lineIdx] != " ":
                stacks[stackIdx].append(line[lineIdx])

    for inst in instructions.splitlines():
        # regex search (re.findall()) of inst (,inst) for one or more digits (r"\d+")
        # map results as ints (map(int,) to iterations, fromStack, toStack
        iterations, fromStack, toStack = map(int, re.findall(r"\d+", inst))
        for _ in range(iterations):
            stacks[toStack - 1].insert(0, stacks[fromStack - 1].pop(0))

    # loop through all stacks and add first item to return string
    return "".join(stack[0] for stack in stacks)


def part2(file):
    crates, instructions = file.split("\n\n")
    stacks = [[] for _ in range(9)]

    for line in crates.splitlines():
        for stackIdx, lineIdx in enumerate(range(1, len(line), 4)):
            if line[lineIdx] != " ":
                stacks[stackIdx].append(line[lineIdx])

    for inst in instructions.splitlines():
        iterations, fromStack, toStack = map(int, re.findall(r"\d+", inst))
        # count down from iterations and pop the index
        for i in reversed(range(iterations)):
            stacks[toStack - 1].insert(0, stacks[fromStack - 1].pop(i))

    return "".join(stack[0] for stack in stacks)


data = open("inputs/day05.txt").read()
print(part1(data))
print(part2(data))
