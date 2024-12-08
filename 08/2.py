from collections import defaultdict

with open("../inputs/08.txt", "r") as f:
    mat = [line.replace("\n", "") for line in f.readlines()]
    x = len(mat)
    y = len(mat[0])
    locations = defaultdict(list)
    antinodes = set()
    for i, row in enumerate(mat):
        for j, col in enumerate(row):
            if col != ".":
                locations[col].append((i, j))
    for frequency in locations.keys():
        for a1 in locations[frequency]:
            for a2 in locations[frequency]:
                if a1 != a2:
                    dx = a1[0]-a2[0]
                    dy = a1[1]-a2[1]
                    pos1 = (a1[0]+dx, a1[1]+dy)
                    pos2 = (a2[0]-dx, a2[1]-dy)
                    for mul in range(100):
                        pos1 = (a1[0]+dx*mul, a1[1]+dy*mul)
                        pos2 = (a2[0]-dx*mul, a2[1]-dy*mul)
                        if pos1[0] >= 0 and pos1[0] < x and pos1[1] >= 0 and pos1[1] < y:
                            antinodes.add(pos1)
                        if pos2[0] >= 0 and pos2[0] < x and pos2[1] >= 0 and pos2[1] < y:
                            antinodes.add(pos2)
    print(len(antinodes))
