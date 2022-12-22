test = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

test = test.split("\n")
testing = False

file = open("inputs/day18.txt").read().split("\n")

cubes = set()
for line in test if testing else file:
    x, y, z, = map(int, line.split(","))
    cubes.add((x, y, z))

directions = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]


def part1(cubes):
    surfaceArea = 0
    for x, y, z in cubes:
        surfaceArea += 6
        for dx, dy, dz in directions:
            if (x+dx, y+dy, z+dz) in cubes:
                surfaceArea -= 1

    return surfaceArea


def part2():
    area = {(x, y, z) for x in range(22) for y in range(22) for z in range(22)}

    air = list(area - cubes)
    airPockets = []

    while air:
        checkList = [air[0]]
        bubble = set()

        while checkList:
            currentPoint = checkList.pop()

            if currentPoint in air:  # check if point have been evaluated or is solid
                bubble.add(currentPoint)
                air.remove(currentPoint)

                x, y, z = currentPoint
                for dx, dy, dz in directions:
                    checkList.append((x+dx, y+dy, z+dz))

        if (0, 0, 0) not in bubble:  # check if the bubble was outside of the blob
            airPockets.append(bubble)

    totalSurfaceArea = part1(cubes)
    airPocketSurfaceArea = sum(part1(pocket) for pocket in airPockets)

    print(totalSurfaceArea - airPocketSurfaceArea)


print(part1(cubes))
part2()
