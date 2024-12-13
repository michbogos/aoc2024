import re
import sympy
from sympy import Rational
import math

import sympy.core
import sympy.solvers

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
            x = sympy.Matrix([Rational(int(num)+10000000000000) for num in digit_pat.findall(line, -1)])
            mat = sympy.Matrix([[Rational(a[0]), Rational(b[0])],[Rational(a[1]), Rational(b[1])]])
            apress, bpress = sympy. symbols("apress, bpress")
            sol = list(sympy.solvers.linsolve((mat, x), [apress, bpress]))[0]
            if sol[0].is_integer and sol[1].is_integer:
                res += 3*int(sol[0])
                res += int(sol[1])
    print(int(res))