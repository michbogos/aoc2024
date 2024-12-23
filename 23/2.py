from sys import stdin
from collections import defaultdict

graph = defaultdict(set)

def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph
        )
        X.add(v)

for line in stdin:
    a, b = line.replace("\n", "").split("-")
    graph[a].add(b)
    graph[b].add(a)

all_cliques = sorted(list(bron_kerbosch(set(), set(graph.keys()), set(), graph)), key=lambda x:len(x))

print(",".join(sorted(all_cliques[-1])))