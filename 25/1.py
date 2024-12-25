from sys import stdin

mat = []
keys = []
locks = []

res = 0

for line in stdin:
    line = line.replace("\n", "")
    if line == "":
        if list(set(mat[0])) == ["#"]:
            locks.append([[mat[i][j] for i in range(len(mat))].count("#") for j in range(len(mat[0]))])
            mat = []
        else:
            keys.append([[mat[i][j] for i in range(len(mat))].count("#") for j in range(len(mat[0]))])
            mat = []
    else:
        mat.append(line)
    


for key in keys:
    for lock in locks:
        works = True
        for i in range(len(lock)):
            if lock[i]+key[i] > 7:
                works = False
        if works:
            res += 1

print(res)