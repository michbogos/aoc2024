import re
from functools import reduce
from operator import mul

with open('../inputs/03.txt', "r") as f:
    s = 0
    p = re.compile(r"mul\(\d*,\d*\)")
    p1 = re.compile(r"do\(\)")
    p2 = re.compile(r"don't\(\)")
    program = "".join(f.readlines())
    prog = []

    dos = [("do", match.start(0)) for match in p1.finditer(program)]
    donts = [("dont", match.start(0)) for match in p2.finditer(program)]
    muls = [(match.group(), match.start(0)) for match in p.finditer(program)]
    dos.extend(donts)
    dos.extend(muls)
    dos.sort(key=lambda x:x[1])
    should_do = True
    for command in dos:
        if command[0] == "do":
            should_do = True
        if command[0] == "dont":
            should_do = False
        if command[0][:3] == "mul" and should_do:
            s += reduce(mul, [int(i) for i in command[0].replace("mul(", "").replace(")", "").split(",")])
    
    print(s)

