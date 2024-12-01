with open("../inputs/01.txt", "r") as f:
    l = []
    r = []
    for line in f.readlines():
        a, b = line.split("  ")
        l.append(int(a))
        r.append(int(b))
    l.sort()
    r.sort()
    print(sum([abs(a-b) for a, b in zip(l, r)]))