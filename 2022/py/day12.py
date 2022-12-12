test = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]
grid = {}
end = None


def shortestPath(start, end):
    allPaths = [[start]]
    i = 0  # index
    pastNodes = {start}

    while i < len(allPaths):
        # read the connections in the dictionary of the latest node in allPaths[i]
        connections = grid[allPaths[i][-1]]

        if end in connections:
            return len(allPaths[i])

        # add new paths
        for node in connections:
            if not node in pastNodes:
                newPath = allPaths[i].copy()
                newPath.append(node)
                allPaths.append(newPath)
                pastNodes.add(node)

        i += 1
    # no path
    return -1


def part1(data):
    global end
    start = None
    for y, line in enumerate(data):
        for x, spot in enumerate(line):
            # change S and E to a and z
            # save start and end locations
            if spot == "S":
                start = (x, y)
                data[y] = data[y].replace("S", "a")
            elif spot == "E":
                end = (x, y)
                data[y] = data[y].replace("E", "z")
    for y, line in enumerate(data):
        for x, spot in enumerate(line):
            grid.update({(x, y): []})  # dictionary of (location:[connections])
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                #border check
                if 0 <= x + dx < len(line) and 0 <= y + dy < len(data):
                    # chr(ord(spot) + 1) --- ord turns the char to unicode then we add 1 and chr turns it back to a char
                    # add 1 because we can only go up 1 elevation at a time
                    if data[y + dy][x + dx] <= chr(ord(spot) + 1):
                        grid[(x, y)].append((x + dx, y + dy))
    return shortestPath(start, end)


def part2(data):
    start = []
    for y, line in enumerate(data):
        for x, spot in enumerate(line):
            if spot == "a":  # add all 'a's to a list
                start.append((x, y))
    return min(shortestPath(i, end) for i in start if shortestPath(i, end) > 0)


heightmap = open("inputs/day12.txt").read().strip().split("\n")
print(part1(heightmap))
print(part2(heightmap))
