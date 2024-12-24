from sys import stdin
from collections import defaultdict

revops = defaultdict(tuple)
node_vals = defaultdict(lambda:-1)

while (line:=stdin.readline()) != "\n":
    k, v = line.replace("\n", "").split(": ")
    v = int(v)
    node_vals[k] = v

start_nodes = node_vals.keys()

zs = set()

for line in stdin:
    a, op, b = line.replace("\n", "").split(" ")[:3]
    res = line.replace("\n", "").split(" ")[-1]
    if res[0] == "z":
        zs.add(res)
    revops[res] = (a, op, b)


def calculate(node, rev):
    if node in start_nodes:
        return node_vals[node]
    a, op, b = rev[node]
    aval = calculate(a, rev)
    bval = calculate(b, rev)
    if op == "AND":
        return int(aval and bval)
    if op == "OR":
        return int(aval or bval)
    if op == "XOR":
        return int(aval != bval)

print(sum(val*2**idx for idx, val in enumerate([calculate(z, revops) for z in sorted(zs)])))