import re
test = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

grid = [["." for _ in range(400)] for _ in range(200)]
xMod = 300
yMax = 0
sandStartx, sandStarty = 500-xMod, 0


def drawMap(data):
    global yMax
    data = data.split("\n")
    for line in data:
        points = list(map(int, re.findall(r"\d+", line)))
        for i in range(0, len(points)-3, 2):
            sx = points[i]-xMod
            sy = points[i+1]
            ex = points[i+2]-xMod
            ey = points[i+3]
            if sx > ex:
                ex, sx = sx, ex
            if sy > ey:
                ey, sy = sy, ey
            for dx in range(ex-sx+1):
                for dy in range(ey-sy+1):
                    yMax = max(sy+dy, yMax)
                    grid[sy+dy][sx+dx] = "#"


def simulate(arg):
    global yMax
    for i in range(len(grid[yMax+2])):
        grid[yMax+2][i] = "#"
    units = 0
    while grid[sandStarty][sandStartx] != "O":
        sandx, sandy = sandStartx, sandStarty
        while True:
            while grid[sandy+1][sandx] == ".":
                sandy += 1
                if sandy >= yMax and arg == "part1":
                    return units
            if grid[sandy+1][sandx-1] == ".":
                sandx -= 1
                sandy += 1
                continue
            elif grid[sandy+1][sandx+1] == ".":
                sandx += 1
                sandy += 1
                continue
            units += 1
            grid[sandy][sandx] = "O"
            break
    return units

data = open("inputs/day14.txt").read().strip()
drawMap(data)
print(simulate("part1"))  # change arg for part2
