keyCycles = [20, 60, 100, 140, 180, 220, 1000]
screen = [[" " for _ in range(40)] for _ in range(6)]


def part1(data):
    cycle = 1
    value = 1
    signalStrength = 0
    for instructions in data:
        cycle += 1  # every instruction goes up at least one cycle
        if instructions[0] == "a":  # addx instruction
            _, v = instructions.split()
            if cycle + 1 > keyCycles[0]:
                signalStrength += keyCycles.pop(0) * value
            cycle += 1
            value += int(v)
    return signalStrength


def part2(data):
    pixel = 0
    spritePosition = 1
    for line in data:
        draw(pixel, spritePosition)
        pixel += 1
        if line[0] == "a":
            _, v = line.split()
            draw(pixel, spritePosition)
            pixel += 1
            spritePosition += int(v)
    for line in screen:
        print(*line)


def draw(pixel, spritePosition):
    if abs(spritePosition - pixel % 40) < 2:
        screen[pixel // 40][pixel % 40] = "#"


data = open("inputs/day10.txt").read().strip().splitlines()
print(part1(data))
part2(data)
