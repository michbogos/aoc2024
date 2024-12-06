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
    mat = [[ch for ch in line.replace("\n", "")] for line in f.readlines()]
    visited = []
    pos = (0, 0)
    direction = (-1, 0)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "^":
                pos = (i, j)
    visited.append(pos)
    
    while True:
        if pos[1] < 0 or pos[1] < 0:
            del visited[-1]
            break
        try:
            if mat[pos[0]+direction[0]][pos[1]+direction[1]] == "#":
                direction = right(direction)
            elif mat[pos[0]+direction[0]][pos[1]+direction[1]] != "#":
                pos=(pos[0]+direction[0], pos[1]+direction[1])
                visited.append(pos)
        except IndexError:
            break
    print(len(set(visited)))