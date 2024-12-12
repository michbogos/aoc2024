from collections import defaultdict

with open("../inputs/12.txt", "r") as f:
    mat = [[c for c in line.replace("\n", "")] for line in f.readlines()]

    res = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != ".":
                perim = 0
                area = 0
                start = [i, j]
                nodes = [start]
                crop = mat[start[0]][start[1]]
                visited = set()
                used_edges = set()
                while len(nodes) > 0:
                    cur = nodes[0]
                    del nodes[0]
                    if tuple(cur) not in visited:
                        area += 1
                        visited.add(tuple(cur))
                        for next in [(cur[0]+1, cur[1]), (cur[0]-1, cur[1]), (cur[0], cur[1]+1), (cur[0], cur[1]-1)]:
                            if next[0] > -1 and next[0] < len(mat) and next[1] > -1 and next[1] < len(mat[0]):
                                if mat[next[0]][next[1]] != crop and (tuple(cur), tuple(next)) not in used_edges and tuple(next) not in visited:
                                    used_edges.add((tuple(cur), tuple(next)))
                                if tuple(next) not in visited and mat[next[0]][next[1]] == crop:
                                    nodes.append(next)
                            else:
                                if (tuple(cur), tuple(next)) not in used_edges:
                                    used_edges.add((tuple(cur), tuple(next)))
                        mat[cur[0]][cur[1]] = "."
                mat_dict = defaultdict(bool)
                for v in visited:
                    mat_dict[v] = True
                vertices = 0
                minx = min(100000, *[v[0] for v in visited])
                miny = min(100000, *[v[1] for v in visited])
                maxx = max(-100000, *[v[0] for v in visited])
                maxy = max(-100000, *[v[1] for v in visited])
                for x in range(minx-1, maxx+1):
                    for y in range(miny-1, maxy+1):
                        v1 = mat_dict[(x, y)]
                        v2 = mat_dict[(x+1, y)]
                        v3 = mat_dict[(x, y+1)]
                        v4 = mat_dict[(x+1, y+1)]
                        if sum([int(v1), int(v2), int(v3), int(v4)])==1 or sum([int(v1), int(v2), int(v3), int(v4)])==3:
                            vertices += 1
                        if ((int(v1)+int(v4))==2 and (int(v2)+int(v3))==0) or ((int(v1)+int(v4))==0 and (int(v2)+int(v3))==2):
                            vertices += 2
                
                res += vertices*len(visited)
    
    print(res)