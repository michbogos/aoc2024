from sys import stdin
from collections import defaultdict


res = 0
resd = defaultdict(int)

for line in stdin:
    d = defaultdict(int)
    num = int(line)
    nums = []
    diffs = []
    for i in range(2000):
        numm = num
        num=(num^(num << 6))%16777216
        num=(num^(num >> 5))%16777216
        num=(num^(num << 11))%16777216
        diffs.append((num%10)-(numm%10))
        nums.append(numm%10)

    nums.append(num%10)
    
    # del diffs[-1]
    # print(nums)
    # print(diffs)

    seen = set()

    for diff, num in zip(zip(diffs, diffs[1:], diffs[2:], diffs[3:]), nums[4:]):
        if diff not in seen:
            d[diff] = num
            seen.add(diff)
    
    for k in d:
        resd[k] += d[k]



print(res:=max([resd[k] for k in resd]))
for k in resd:
    if resd[k] == res:
        print(k)