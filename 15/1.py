with open("../inputs/15.txt", "r") as f:
    mat = []
    while (line:=f.readline()) != "\n":
        mat.append([c for c in line.replace("\n", "")])
    instructions = ""
    while line:=f.readline():
        instructions+=line.replace("\n", "")
    
    pos = []

    for line in mat:
        print("".join(line))
    
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "@":
                mat[i][j] = "."
                pos = [i, j]
    
    print(pos)
    
    for c in instructions:
        if c == "^":
            if mat[pos[0]-1][pos[1]] == ".":
                pos[0] -= 1
            elif mat[pos[0]-1][pos[1]] == "O":
                i = 1
                barrels = []
                while True:
                    if mat[pos[0]-1*i][pos[1]] == "O":
                        barrels.append([pos[0]-1*i, pos[1]])
                    elif mat[pos[0]-1*i][pos[1]] == ".":
                        for barrel in reversed(barrels):
                            mat[barrel[0]-1][barrel[1]] = "O"
                            mat[barrel[0]][barrel[1]] = "."
                        pos[0] -= 1
                        break
                    elif mat[pos[0]-1*i][pos[1]] == "#":
                        break
                    i += 1
            elif mat[pos[0]-1][pos[1]] == "#":
                pass
        if c == ">":
            if mat[pos[0]][pos[1]+1] == ".":
                pos[1] += 1
            elif mat[pos[0]][pos[1]+1] == "O":
                i = 1
                barrels = []
                while True:
                    if mat[pos[0]][pos[1]+1*i] == "O":
                        barrels.append([pos[0], pos[1]+1*i])
                    elif mat[pos[0]][pos[1]+1*i] == ".":
                        for barrel in reversed(barrels):
                            mat[barrel[0]][barrel[1]+1] = "O"
                            mat[barrel[0]][barrel[1]] = "."
                        pos[1] += 1
                        break
                    elif mat[pos[0]][pos[1]+1*i] == "#":
                        break
                    i += 1
            elif mat[pos[0]][pos[1]+1] == "#":
                pass
        if c == "v":
            if mat[pos[0]+1][pos[1]] == ".":
                pos[0] += 1
            elif mat[pos[0]+1][pos[1]] == "O":
                i = 1
                barrels = []
                while True:
                    if mat[pos[0]+1*i][pos[1]] == "O":
                        barrels.append([pos[0]+1*i, pos[1]])
                    elif mat[pos[0]+1*i][pos[1]] == ".":
                        for barrel in reversed(barrels):
                            mat[barrel[0]+1][barrel[1]] = "O"
                            mat[barrel[0]][barrel[1]] = "."
                        pos[0] += 1
                        break
                    elif mat[pos[0]+1*i][pos[1]] == "#":
                        break
                    i += 1
            elif mat[pos[0]+1][pos[1]] == "#":
                pass
        if c == "<":
            if mat[pos[0]][pos[1]-1] == ".":
                pos[1] -= 1
            elif mat[pos[0]][pos[1]-1] == "O":
                i = 1
                barrels = []
                while True:
                    if mat[pos[0]][pos[1]-1*i] == "O":
                        barrels.append([pos[0], pos[1]-1*i])
                    elif mat[pos[0]][pos[1]-1*i] == ".":
                        for barrel in reversed(barrels):
                            mat[barrel[0]][barrel[1]-1] = "O"
                            mat[barrel[0]][barrel[1]] = "."
                        pos[1] -= 1
                        break
                    elif mat[pos[0]][pos[1]-1*i] == "#":
                        break
                    i += 1
            elif mat[pos[0]][pos[1]-1] == "#":
                pass 
    res = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 'O':
                res += 100*i+j
    
    for line in mat:
        print("".join(line))
    print(res)