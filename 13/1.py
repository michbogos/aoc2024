import re
import numpy
import math

with open("../inputs/13.txt", "r") as f:
    res = 0
    digit_pat = re.compile(r"\d+")
    a = []
    b = []
    x = []
    y = []
    for i, line in enumerate(f.readlines()):
        if i%4 == 0:
            a = [int(num) for num in digit_pat.findall(line, -1)]
        if i%4 == 1:
            b = [int(num) for num in digit_pat.findall(line, -1)]
        if i%4 == 2:
            x = [int(num) for num in digit_pat.findall(line, -1)]
            print(a, b, x)
            apress, bpress = numpy.linalg.solve([[a[0], b[0]], [a[1], b[1]]], x)
            if abs(round(apress)-apress) < 0.00001:
                res += 3*apress
            if abs(round(bpress)-bpress) < 0.00001:
                res += 1*bpress
    print(int(res))