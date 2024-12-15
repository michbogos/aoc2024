with open("../inputs/15.txt", "r") as f:
    mat = []
    while (line:=f.readline()) != "\n":
        mat.append([c for c in line.replace("\n", "").replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")])
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
            elif mat[pos[0]-1][pos[1]] in "[]":
                barrels = set()
                if mat[pos[0]-1][pos[1]] == "[":
                    barrels = set([(pos[0]-1, pos[1]), (pos[0]-1, pos[1]+1)])
                else:
                    barrels = set([(pos[0]-1, pos[1]), (pos[0]-1, pos[1]-1)])
                added = True
                obstacle = False
                while added:
                    added = False
                    for barrel in list(barrels):
                        if mat[barrel[0]-1][barrel[1]] == "[" and (barrel[0]-1,barrel[1]) not in barrels:
                            barrels.add((barrel[0]-1, barrel[1]))
                            barrels.add((barrel[0]-1, barrel[1]+1))
                            added = True
                        elif mat[barrel[0]-1][barrel[1]] == "]" and (barrel[0]-1,barrel[1]) not in barrels:
                            barrels.add((barrel[0]-1, barrel[1]))
                            barrels.add((barrel[0]-1, barrel[1]-1))
                            added = True
                        elif mat[barrel[0]-1][barrel[1]] == "#":
                            obstacle = True
                            added = False
                            break
                    if obstacle:
                         break
                if not obstacle:
                    for barrel in sorted(list(barrels), key=lambda x:x[0]):
                        mat[barrel[0]-1][barrel[1]] = mat[barrel[0]][barrel[1]]
                        mat[barrel[0]][barrel[1]] = "."
                    pos[0] -= 1

            elif mat[pos[0]-1][pos[1]] == "#":
                pass
        if c == ">":
            if mat[pos[0]][pos[1]+1] == ".":
                pos[1] += 1
            elif mat[pos[0]][pos[1]+1] in "[]":
                i = 1
                barrels = []
                while True:
                    if mat[pos[0]][pos[1]+1*i] in "[]":
                        barrels.append([pos[0], pos[1]+1*i])
                    elif mat[pos[0]][pos[1]+1*i] == ".":
                        for barrel in reversed(barrels):
                            mat[barrel[0]][barrel[1]+1] = mat[barrel[0]][barrel[1]]
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
            elif mat[pos[0]+1][pos[1]] in "[]":
                barrels = set()
                if mat[pos[0]+1][pos[1]] == "[":
                    barrels = set([(pos[0]+1, pos[1]), (pos[0]+1, pos[1]+1)])
                else:
                    barrels = set([(pos[0]+1, pos[1]), (pos[0]+1, pos[1]-1)])
                added = True
                obstacle = False
                while added:
                    added = False
                    for barrel in list(barrels):
                        if mat[barrel[0]+1][barrel[1]] == "[" and (barrel[0]+1,barrel[1]) not in barrels:
                            barrels.add((barrel[0]+1, barrel[1]))
                            barrels.add((barrel[0]+1, barrel[1]+1))
                            added = True
                        elif mat[barrel[0]+1][barrel[1]] == "]" and (barrel[0]+1,barrel[1]) not in barrels:
                            barrels.add((barrel[0]+1, barrel[1]))
                            barrels.add((barrel[0]+1, barrel[1]-1))
                            added = True
                        elif mat[barrel[0]+1][barrel[1]] == "#":
                            obstacle = True
                            break
                if not obstacle:
                    for barrel in sorted(list(barrels), key=lambda x:x[0], reverse=True):
                        mat[barrel[0]+1][barrel[1]] = mat[barrel[0]][barrel[1]]
                        mat[barrel[0]][barrel[1]] = "."
                    pos[0] += 1

            elif mat[pos[0]+1][pos[1]] == "#":
                pass
        if c == "<":
            if mat[pos[0]][pos[1]-1] == ".":
                pos[1] -= 1
            elif mat[pos[0]][pos[1]-1] in "[]":
                i = 1
                barrels = []
                while True:
                    if mat[pos[0]][pos[1]-1*i] in "[]":
                        barrels.append([pos[0], pos[1]-1*i])
                    elif mat[pos[0]][pos[1]-1*i] == ".":
                        for barrel in reversed(barrels):
                            mat[barrel[0]][barrel[1]-1] = mat[barrel[0]][barrel[1]]
                            mat[barrel[0]][barrel[1]] = "."
                        pos[1] -= 1
                        break
                    elif mat[pos[0]][pos[1]-1*i] == "#":
                        break
                    i += 1
            elif mat[pos[0]][pos[1]-1] == "#":
                pass 
        # for line in mat:
        #     print("".join(line))
    res = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '[':
                res += 100*i+j
    
    for line in mat:
        print("".join(line))
    print(res)