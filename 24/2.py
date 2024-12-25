from sys import stdin
from collections import defaultdict
import graphviz

revops = defaultdict(tuple)
node_vals = defaultdict(lambda:-1)

graph = graphviz.Digraph()
idx = 0

while (line:=stdin.readline()) != "\n":
    k, v = line.replace("\n", "").split(": ")
    v = int(v)
    node_vals[k] = v
    graph.node(k, k)

for line in stdin:
    a, op, b = line.replace("\n", "").split(" ")[:3]
    res = line.replace("\n", "").split(" ")[-1]
    graph.node(res, res)
    graph.edge(a, res)
    graph.edge(b, res)

graph.render('graph.gv', view=True) 
