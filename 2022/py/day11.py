import re


def part1(data):
    items = [[] for _ in range(len(data))]
    inspections = [0] * (len(data))
    for m, monkey in enumerate(data):
        monkey = monkey.split("\n")
        items[m] = list(map(int, re.findall(r"\d+", monkey[1])))
    for round in range(20):
        for m, monkey in enumerate(data):
            monkey = monkey.split("\n")
            op = monkey[2].split()[-2:]
            test = int(monkey[3].split()[-1])
            t = int(monkey[4].split()[-1])
            f = int(monkey[5].split()[-1])
            for i in range(len(items[m])):
                inspections[m] += 1
                if op[0] == "*":
                    if op[1] == "old":
                        items[m][i] *= items[m][i]
                    else:
                        items[m][i] *= int(op[1])
                else:
                    if op[1] == "old":
                        items[m][i] += items[m][i]
                    else:
                        items[m][i] += int(op[1])
                items[m][i] = items[m][i] // 3
                if items[m][i] % test == 0:
                    items[t].append(items[m][i])
                else:
                    items[f].append(items[m][i])
            items[m] = []
    inspections.sort()
    return inspections[-1] * inspections[-2]


def part2(data):
    inspections = [0] * (len(data))
    monkeyData = []
    mod = 1
    for monkey in data:
        monkey = monkey.split("\n")
        mod *= int(monkey[3].split()[-1])
        monkeyData.append(
            {
                "items": list(map(int, re.findall(r"\d+", monkey[1]))),
                "op": monkey[2].split()[-2:],
                "test": int(monkey[3].split()[-1]),
                "t": int(monkey[4].split()[-1]),
                "f": int(monkey[5].split()[-1]),
            }
        )

    for round in range(10000):
        for m, monkey in enumerate(monkeyData):
            for item in monkey["items"]:
                inspections[m] += 1
                if monkey["op"][0] == "*":
                    if monkey["op"][1] == "old":
                        item *= item
                    else:
                        item *= int(monkey["op"][1])
                else:
                    if monkey["op"][1] == "old":
                        item += item
                    else:
                        item += int(monkey["op"][1])
                item = item % mod
                if item % monkey["test"] == 0:
                    monkeyData[monkey["t"]]["items"].append(item)
                else:
                    monkeyData[monkey["f"]]["items"].append(item)
            monkey["items"] = []
    inspections.sort()
    return inspections[-1] * inspections[-2]


monkeys = open("inputs/day11.txt").read().strip().split("\n\n")
print(part1(monkeys))
print(part2(monkeys))
