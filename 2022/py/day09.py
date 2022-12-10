direction = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}


def part1(data):
    locations = {(0, 0)}
    hx, hy = 0, 0  # head
    tx, ty = 0, 0  # tail
    for line in data:
        d, amount = line.split(" ")
        dx, dy = direction[d]  # movement direction
        for _ in range(int(amount)):
            hx += dx  # move head
            hy += dy
            if abs(hx - tx) > 1:
                tx += 1 if hx > tx else -1
                if abs(hy - ty) > 0:
                    ty += 1 if hy > ty else -1
            elif abs(hy - ty) > 1:
                ty += 1 if hy > ty else -1
                if abs(hx - tx) > 0:
                    tx += 1 if hx > tx else -1
            locations.add((tx, ty))
    return len(locations)


def part2(data):
    locations = {(0, 0)}
    rope = [(0, 0)] * 10
    for line in data:
        d, amount = line.split(" ")
        dx, dy = direction[d]
        for _ in range(int(amount)):
            hx, hy = rope[0]
            rope[0] = tuple((hx + dx, hy + dy))  # move head first
            for i in range(1, len(rope)):
                hx, hy = rope[i - 1]
                tx, ty = rope[i]  # move each knot as a tail to the previous
                if abs(hx - tx) > 1:
                    tx += 1 if hx > tx else -1
                    if abs(hy - ty) > 0:
                        ty += 1 if hy > ty else -1
                elif abs(hy - ty) > 1:
                    ty += 1 if hy > ty else -1
                    if abs(hx - tx) > 0:
                        tx += 1 if hx > tx else -1
                rope[i] = tx, ty
            locations.add(rope[-1])  # only add location of last knot
    return len(locations)


data = open("inputs/day09.txt").read().strip().splitlines()
print(part1(data))
print(part2(data))
