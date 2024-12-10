visited = []

def dfs(pos, mat, count):
    for next in [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]:
        if next[0] > -1 and next[0] < len(mat) and next[1] > -1 and next[1] < len(mat[0]) and not visited[next[0]][next[1]] and int(mat[next[0]][next[1]])-int(mat[pos[0]][pos[1]]) == 1:
            visited[next[0]][next[1]] = True
            if mat[next[0]][next[1]] == "9":
                count += 1
            count = dfs(next, mat, count)
    return count

with open("../inputs/10.txt", "r") as f:
    mat = [line.replace("\n", "") for line in f.readlines()]
    zeroes = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "0":
                zeroes.append((i, j))
    
    count = 0
    
    for zero in zeroes:
        visited = [[False for _ in line] for line in mat]
        count += dfs(zero, mat, 0)
    
    print(count)
        