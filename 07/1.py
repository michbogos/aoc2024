import re

with open("../inputs/07.txt") as f:
    p = re.compile(r"\d+")
    s = 0
    for line in f.readlines():
        nums = [int(num) for num in p.findall(line, -1)]
        target = nums[0]
        del nums[0]

        for i in range(2**(len(nums)-1)):
            res = nums[0]
            for j, op in enumerate(format(i, f"0{len(nums)-1}b")):
                if bool(int(op)):
                    res += nums[j+1]
                if not bool(int(op)):
                    res *= nums[j+1]
            if res == target:
                s += target
                break
    print(s)