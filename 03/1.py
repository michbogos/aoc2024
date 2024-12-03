import re
from functools import reduce
from operator import mul

with open('../inputs/03.txt', "r") as f: print(sum([reduce(mul, [int(num) for num in match.replace("(", "").replace(")", "").replace("mul", "").split(",")]) for match in re.compile(r"mul\(\d*,\d*\)").findall("".join(f.readlines()))]))
