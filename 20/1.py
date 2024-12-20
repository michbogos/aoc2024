from heapq import heapify, heappush, heappop
from copy import deepcopy

with open("../inputs/20.txt", "r") as f:
    res = 0
    mat = [[c for c in line.replace("\n", "")] for line in f.readlines()]
    start = (0, 0)
    end = (0, 0)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "S":
                start = (i, j)
            if mat[i][j] == "E":
                end = (i, j)
    
    shortest = 0
    heap = []
    dist = [[10e10 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    nxt = [[() for _ in range(len(mat[0]))] for _ in range(len(mat))]
    dist[start[0]][start[1]] = 0
    heappush(heap, (0, start[0], start[1]))
    while len(heap) > 0:
        node = heappop(heap)
        for dx in [-1, 1]:
            next = (node[1], node[2]+dx)
            if mat[next[0]][next[1]] != "#":
                if dist[next[0]][next[1]] > node[0]+1:
                    dist[next[0]][next[1]] = node[0]+1
                    nxt[node[1]][node[2]] = (next[0], next[1])
                    heappush(heap, (node[0]+1, next[0], next[1]))
        for dy in [-1, 1]:
            next = (node[1]+dy, node[2])
            if mat[next[0]][next[1]] != "#":
                if dist[next[0]][next[1]] > node[0]+1:
                    dist[next[0]][next[1]] = node[0]+1
                    nxt[node[1]][node[2]] = (next[0], next[1])
                    heappush(heap, (node[0]+1, next[0], next[1]))
    
    shortest = dist[end[0]][end[1]]

    path = set(start)

    node = start
    while node != end:
        path.add((nxt[node[0]][node[1]]))
        node = nxt[node[0]][node[1]]
    node = start
    while node != end:
        for dx in [2,-2]:
            if node[1]+dx > -1 and node[1]+dx < len(mat[0]) and (node[0],node[1]+dx) in path:
                if mat[node[0]][node[1]+dx] != "#" and (dist[node[0]][node[1]+dx])-dist[node[0]][node[1]]-1 >= 100 and dist[node[0]][node[1]+dx] < 10e9:
                    res += 1
        # for dx in [3,-3]:
        #     if node[1]+dx > -1 and node[1]+dx < len(mat[0]):
        #         if mat[node[0]][node[1]+dx] == "." and (dist[node[0]][node[1]+dx])-dist[node[0]][node[1]]-3 == 6 and dist[node[0]][node[1]+dx] < 10e9:
        #             res += 1
        
        for dy in [2,-2]:
            if node[0]+dy > -1 and node[0]+dy < len(mat) and (node[0]+dy,node[1]) in path:
                if mat[node[0]+dy][node[1]] != "#" and (dist[node[0]+dy][node[1]])-dist[node[0]][node[1]]-1 >= 100 and dist[node[0]+dy][node[1]] < 10e9:
                    res += 1
        # for dy in [3,-3]:
        #     if node[0]+dy > -1 and node[0]+dy < len(mat):
        #         if mat[node[0]+dy][node[1]] == "." and (dist[node[0]+dy][node[1]])-dist[node[0]][node[1]]-3 == 6 and dist[node[0]+dy][node[1]] < 10e9:
        #             res += 1
        
        node = nxt[node[0]][node[1]]
                    
    
    print(res)


