with open("../inputs/10.txt", "r") as f:
    mat = [line.replace("\n", "") for line in f.readlines()]
    zeroes = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "0":
                zeroes.append((i, j))
    
    count = 0
    for zero in zeroes:
        nodes = [zero]
        while len(nodes) > 0:
            pos = nodes[-1]
            del nodes[-1]
            for next in [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]:
                if next[0] > -1 and next[0] < len(mat) and next[1] > -1 and next[1] < len(mat[0]) and int(mat[next[0]][next[1]])-int(mat[pos[0]][pos[1]]) == 1:
                    nodes.append(next)
                    if mat[next[0]][next[1]] == "9":
                        count += 1
    print(count)