def part1(data):
    visible = 0
    for treeY, row in enumerate(data):
        for treeX, height in enumerate(row):
            # treeX,Y is the trees location, height is its value
            visible += (
                # check if all trees in each direction are shorter, add the true/false
                all(data[treeY][x] < height for x in range(0, treeX))
                or all(data[treeY][x] < height for x in range(treeX + 1, len(row)))
                or all(data[y][treeX] < height for y in range(0, treeY))
                or all(data[y][treeX] < height for y in range(treeY + 1, len(data)))
            )
    return visible


def part2(data):
    scores = []
    for treeY, row in enumerate(data):
        for treeX, height in enumerate(row):
            siteScore = 1
            direction = 0
            # check one direction until a tree height is >= current height
            for x in range(treeX - 1, -1, -1):
                direction += 1
                if data[treeY][x] >= height:
                    break
            # multiply the directions score by the current siteScore
            siteScore *= direction
            direction = 0
            for x in range(treeX + 1, len(row)):
                direction += 1
                if data[treeY][x] >= height:
                    break
            siteScore *= direction
            direction = 0
            for y in range(treeY - 1, -1, -1):
                direction += 1
                if data[y][treeX] >= height:
                    break
            siteScore *= direction
            direction = 0
            for y in range(treeY + 1, len(data)):
                direction += 1
                if data[y][treeX] >= height:
                    break
            siteScore *= direction
            scores.append(siteScore)
    # iterate through each score and return the max
    return max(score for score in scores)


data = open("inputs/day08.txt").read().strip().splitlines()
print(part1(data))
print(part2(data))
