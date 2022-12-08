class Folder:
    def __init__(self,  parent):
        self.parent = parent
        self.size = 0

    def increase(self, addon):
        self.size += addon
        if self.parent != None:
            self.parent.increase(addon)


dir = []


def part1(data):
    cwd = Folder(None)
    dir.append(cwd)
    for line in data:
        match line.split():
            case ["$", "cd", "/"]:
                continue
            case ["$", "cd", ".."]:
                cwd = cwd.parent
            case ["$", "cd", _]:
                cwd = Folder(cwd)
                dir.append(cwd)
            case [size, _] if size.isdigit():
                cwd.increase(int(size))
    return sum(x.size for x in dir if x.size < 100000)


def part2():
    return min(x.size for x in dir if x.size > dir[0].size-40000000)


data = open("inputs/day07.txt").read().splitlines()
print(part1(data))
print(part2())
