with open("12.txt", "r") as f:
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


                edges = set([(edge[0], edge[1], (edge[1][0]-edge[0][0], edge[1][1]-edge[0][1])) for edge in used_edges])
                sides = 0
                while len(edges) > 0:
                    a = edges.pop()
                    b = a
                    added = True
                    while added:
                        added = False
                        for edge in edges:
                            if edge[2] == b[2]:
                                if b[2] == (1, 0):
                                    if edge[0][1]-b[0][1]==1:
                                        b = edge
                                        edges.remove(edge)
                                        added = True
                                        break
                                    if edge[0][1]-a[0][1]==-1:
                                        a = edge
                                        edges.remove(edge)
                                        added = True
                                        break
                                if b[2] == (-1, 0):
                                    if edge[0][1]-b[0][1]==1:
                                        b = edge
                                        edges.remove(edge)
                                        added = True
                                        break
                                    if edge[0][1]-a[0][1]==-1:
                                        a = edge
                                        edges.remove(edge)
                                        added = True
                                        break
                                if b[2] == (0, 1):
                                    if edge[0][0]-b[0][0]==1:
                                        b = edge
                                        edges.remove(edge)
                                        added = True
                                        break
                                    if edge[0][0]-a[0][0]==-1:
                                        a = edge
                                        edges.remove(edge)
                                        added = True
                                        break
                                if b[2] == (0,-1):
                                    if edge[0][0]-b[0][0]==1:
                                        b = edge
                                        edges.remove(edge)
                                        added = True
                                        break
                                    if edge[0][0]-a[0][0]==-1:
                                        a = edge
                                        edges.remove(edge)
                                        added = True
                                        break
                    sides += 1
                            
                print(sides)
                res += len(used_edges)*len(visited)
    
    print(res)