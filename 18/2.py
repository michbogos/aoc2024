from heapq import heapify, heappop, heappush

with open("../inputs/18.txt", "r") as f:
    coords = [[int(i) for i in line.split(",")] for line in f.readlines()]
    # print(coords)
    mat = [[False for _ in range(71)] for _ in range(71)]
    for i in range(1024):
        x, y = coords[i]
        mat[y][x] = True
    
    for coord in coords[1024:]:
        mat[coord[1]][coord[0]] = True
        heap = []
        dist = [[10e10 for _ in range(71)] for _ in range(71)]
        dist[0][0] = 0
        heappush(heap, (0, 0, 0))
        while len(heap):
            node = heappop(heap)
            for dx in [-1, 1]:
                nxt = [node[1], node[2]+dx]
                if nxt[0] > -1 and nxt[0] < 71 and nxt[1] > -1 and nxt[1] < 71 and not mat[nxt[0]][nxt[1]]:
                    if dist[nxt[0]][nxt[1]] > node[0] + 1:
                        dist[nxt[0]][nxt[1]] = node[0] + 1
                        heappush(heap, (node[0] + 1, nxt[0], nxt[1]))

            for dy in [-1, 1]:
                nxt = [node[1]+dy, node[2]]
                if nxt[0] > -1 and nxt[0] < 71 and nxt[1] > -1 and nxt[1] < 71 and not mat[nxt[0]][nxt[1]]:
                    if dist[nxt[0]][nxt[1]] > node[0] + 1:
                        dist[nxt[0]][nxt[1]] = node[0] + 1
                        heappush(heap, (node[0] + 1, nxt[0], nxt[1]))
    
        if dist[-1][-1] > 10000:
            print(",".join([str(c) for c in coord]))
            exit()