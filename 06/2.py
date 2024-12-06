import copy

def right(dir):
    if dir == (1, 0):
        return (0, -1)
    elif dir == (0, 1):
        return (1, 0)
    elif dir == (-1, 0):
        return (0, 1)
    elif dir == (0, -1):
        return (-1, 0)

with open("../inputs/06.txt", "r") as f:
    count = 0
    mat = [[ch for ch in line.replace("\n", "")] for line in f.readlines()]
    visited = set()
    pos = (0, 0)
    direction = (-1, 0)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "^":
                pos = (i, j)

    start = pos

    print(len(mat), len(mat[0]))

    for i in range(len(mat)):
        print(i)
        print("Count:", count)
        for j in range(len(mat[i])):
            if mat[i][j] == ".":
                test_mat = copy.deepcopy(mat)
                test_mat[i][j] = "#"
                visited.clear()
                visited.add(start)
                direction = (-1, 0)
                pos = start
                loop = True
                for step in range(17000*2):
                    if pos[0] < 0 or pos[1] < 0:
                        loop = False
                        break
                    try:
                        if test_mat[pos[0]+direction[0]][pos[1]+direction[1]] == "#":
                            direction = right(direction)
                        else:
                            pos=(pos[0]+direction[0], pos[1]+direction[1])
                            visited.add(pos)
                    except IndexError:
                        loop = False
                        break
                if loop:
                    count += 1
    print(count)