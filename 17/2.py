import re

with open("../inputs/17.txt", "r") as f:
    pat = re.compile(r"-*\d+")
    a = [int(num) for num in pat.findall(f.readline())][0]
    b = [int(num) for num in pat.findall(f.readline())][0]
    c = [int(num) for num in pat.findall(f.readline())][0]
    f.readline()
    code = [int(num) for num in pat.findall(f.readline())]

    res = []
    ip = 0
    a = 16777217
    while ip < len(code)-1:
        if code[ip] == 0:
            op1 = a
            op2 = 0
            if code[ip+1] <= 3:
                op2 = code[ip+1]
            if code[ip+1] == 4:
                op2 = a
            if code[ip+1] == 5:
                op2 = b
            if code[ip+1] == 6:
                op2 = c
            
            a //= 2**op2
            ip += 2
        
        elif code[ip] == 1:
            b = (b^code[ip+1])
            ip += 2
        
        elif code[ip] == 2:
            op2 = 0
            if code[ip+1] <= 3:
                op2 = code[ip+1]
            if code[ip+1] == 4:
                op2 = a
            if code[ip+1] == 5:
                op2 = b
            if code[ip+1] == 6:
                op2 = c
            b = op2%8
            ip += 2
        
        elif code[ip] == 3:
            if a != 0:
                ip = code[ip+1]
            else:
                ip += 2
        
        elif code[ip] == 4:
            b = (b^c)
            ip += 2
        elif code[ip] == 5:
            op2 = 0
            if code[ip+1] <= 3:
                op2 = code[ip+1]
            if code[ip+1] == 4:
                op2 = a
            if code[ip+1] == 5:
                op2 = b
            if code[ip+1] == 6:
                op2 = c
            
            # print(f"{op2%8}, ")
            print("OP2:", op2)
            print("a:", a)
            print("OP2:", bin(op2))
            print("a:  ", bin(a))
            res.append(str(op2%8))
            ip += 2
            # print("".join(res))
        
        elif code[ip] == 6:
            op1 = a
            op2 = 0
            if code[ip+1] <= 3:
                op2 = code[ip+1]
            if code[ip+1] == 4:
                op2 = a
            if code[ip+1] == 5:
                op2 = b
            if code[ip+1] == 6:
                op2 = c
            
            b = a // 2**op2
            ip += 2
        
        elif code[ip] == 7:
            op1 = a
            op2 = 0
            if code[ip+1] <= 3:
                op2 = code[ip+1]
            if code[ip+1] == 4:
                op2 = a
            if code[ip+1] == 5:
                op2 = b
            if code[ip+1] == 6:
                op2 = c
            
            c = a // 2**op2
            ip += 2


    # print(a)
    # print(b)
    # print(c)
    # print(code)
    print(",".join(res))