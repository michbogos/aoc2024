import re

def base3(n, length):
    res=[]
    if n == 0:
        return "0"*length
    while n > 0:
        n, r = divmod(n, 3)
        res.append(str(r))
    return (length-len(res))*"0"+"".join(reversed(res))

with open("../inputs/07.txt") as f:
    p = re.compile(r"\d+")
    s = 0
    for linenum, line in enumerate(f.readlines()):
        nums = [int(num) for num in p.findall(line, -1)]
        target = nums[0]
        del nums[0]

        for i in range(3**(len(nums)-1)):
            res = nums[0]
            for j, op in enumerate(base3(i, len(nums)-1)):
                if op == "0":
                    res += nums[j+1]
                if op == "1":
                    res *= nums[j+1]
                if op == "2":
                    res = int(str(res)+str(nums[j+1]))
            if res == target:
                s += target
                break
    print(s)