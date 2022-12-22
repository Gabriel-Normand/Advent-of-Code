import time

startTime = time.time()
data = open("inputs/day15.txt").read().strip().split("\n")

test = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''
test = test.split("\n")
testing = 0  # 0 for data  1 for testing
sensors = []
beacons = []

for line in test if testing else data:
    line = line.split(",")
    sx = int(line[0][12:])
    middle = line[1].split(":")
    sy = int(middle[0][3:])
    bx = int(middle[1][24:])
    by = int(line[2][3:])
    sr = abs(sx-bx)+abs(sy-by)
    sensors.append([sx, sy, sr])
    beacons.append([bx, by])


def part1():
    global sensors, beacons
    X_MIN = -100 if testing else -1_000_000
    X_TARGET = 100 if testing else 6_000_000
    y = 10 if testing else 2_000_000

    counter = 0
    for x in range(X_TARGET, X_MIN, -1):
        flag = 1
        for beacon in beacons:
            if beacon[0] == x and beacon[1] == y:
                flag = 0
                break
        if flag:
            for sensor in sensors:
                sx, sy, sr = sensor
                if manhattanDistance(sx, sy, x, y) <= sr:
                    counter += 1
                    break
    return counter


def part2():
    global sensors, beacons
    MIN = 0
    MAX = 20 if testing else 4_000_000

    for sensor1 in sensors:
        sx1, sy1, sr1 = sensor1
        sr1 += 1  # increase range by 1 to check outer border

        # iterate through each point on the exterior of the sensors range
        for x in range(max(sx1-sr1, MIN), min(sx1+sr1, MAX)+1):  # stay within defined borders
            y = sy1 - (sr1 - abs(sx1 - x))
            if MIN <= y <= MAX:  # stay within defined borders
                # check each point to make sure it is out of other sensor ranges
                for sensor2 in sensors:
                    if sensor2 == sensor1:
                        continue
                    sx2, sy2, sr2 = sensor2
                    if manhattanDistance(sx2, sy2, x, y) <= sr2:
                        location = None
                        break
                    location = x * 4_000_000 + y

            y = sy1 + (sr1 - abs(sx1 - x))  # check other y value on x-axis
            if MIN <= y <= MAX:
                for sensor2 in sensors:
                    if sensor2 == sensor1:
                        continue
                    sx2, sy2, sr2 = sensor2
                    if manhattanDistance(sx2, sy2, x, y) <= sr2:
                        location = None
                        break
                    location = x * 4_000_000 + y

            if location != None:
                return location


def manhattanDistance(x1, y1, x2, y2):
    return abs(x1-x2)+(y1-y2)


initialSetupTime = time.time()
print(part1())
part1Time = time.time()
print(part2())
part2Time = time.time()


print(f"""
Total Time: {part2Time-startTime} seconds
Setup Time: {initialSetupTime-startTime} seconds
Part1 Time: {part1Time-initialSetupTime} seconds
Part2 Time: {part2Time-part1Time} seconds""")
