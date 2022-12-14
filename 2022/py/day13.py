test = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def compare(left, right):
    match (left, right):
        case (int(), int()):
            return left - right

        case (int(), list()):
            return compare([left], right)

        case (list(), int()):
            return compare(left, [right])

        case (list(), list()):
            i = 0
            while i < len(left) and i < len(right):
                c = compare(left[i], right[i])
                i += 1
                if c == 0:
                    continue
                return c
            return len(left) - len(right)


def part1(data):
    total = 0
    for i, packet in enumerate(data.split("\n\n")):
        left, right = packet.split()
        left = eval(left)  # eval does all the work here
        right = eval(right)
        if compare(left, right) < 0:
            total += i + 1
    return total


def part2(data):
    data += "\n[[2]]\n[[6]]"
    decoderkey = 1
    data = data.split("\n")
    data = [i for i in data if i != ""]  # remove blanks
    # need to look into functools.cmp_to_key to use sorted()
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if compare(eval(data[j]), eval(data[j + 1])) > 0:
                data[j], data[j + 1] = data[j + 1], data[j]  # swap
    for i, line in enumerate(data):
        if line == "[[2]]" or line == "[[6]]":
            decoderkey *= i + 1
    return decoderkey


data = open("inputs/day13.txt").read().strip()
print(part1(data))
print(part2(data))
