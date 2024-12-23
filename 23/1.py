from sys import stdin
from collections import defaultdict

graph = defaultdict(set)

for line in stdin:
    a, b = line.replace("\n", "").split("-")
    graph[a].add(b)
    graph[b].add(a)

groups = set()

for k in graph:
    if k[0] == "t":
        for s1 in graph[k]:
            for s2 in graph[k]:
                if s1 in graph[s2] and s1 != s2 and s1 != k and s2 != k:
                    groups.add(tuple(sorted((k, s1, s2))))
print(len(groups))