test = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''

#  DD, BB, JJ, HH, EE, CC - all non 0 valves in order of opening
#  20, 13, 21, 22,  3,  2 - flow rate
#  27  24  20  12   8   5 - minute valve was opened
# 540 310 420 264  24  10 - total pressure relieved
#   1   2   3   6   3   2 - movements taken to get to valve


def part1(rawData):
    valves = {}
    for line in rawData.splitlines():
        parts = line.split()
        valveName = parts[1]
        flowRate = int(parts[4][5:-1])
        connections = "".join(parts[9:]).split(",")
        valves[valveName] = (flowRate, connections)

    allPossibleStates = [("AA", set(), 0)]
    totalTime = 30
    best = {}
    for time in range(1, totalTime+1):
        print(time, len(allPossibleStates))
        nextStates = []
        for location, opened, pressure in allPossibleStates:
            # have we been here before and are things better this time?
            key = (location, ' '.join(sorted(opened)))
            if key in best and pressure <= best[key]:
                continue
            best[key] = pressure

            # get info about this location
            flowRate, connections = valves[location]

            # stay and open a valve for nextState
            if location not in opened and flowRate > 0:
                nextStates.append(
                    (location, opened | {location}, pressure + flowRate*(totalTime-time)))

            # add possible destinations to nextState
            for connection in connections:
                nextStates.append((connection, opened, pressure))

        allPossibleStates = nextStates
    answer = max(pressure for _, _, pressure in allPossibleStates)
    print(answer)


rawData = open("inputs/day16.txt").read().strip()
print(part1(rawData))
# print(part2())
