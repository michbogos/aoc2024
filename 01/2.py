with open("../inputs/01.txt", "r") as f:
    s = 0
    l = []
    r = {}
    for line in f.readlines():
        a, b = line.split("  ")
        l.append(int(a))
        try:
            r[int(b)] += 1
        except KeyError:
            r[int(b)] = 1
    for num in l:
        try:
            s += num*r[num]
        except KeyError:
            pass
    print(s)