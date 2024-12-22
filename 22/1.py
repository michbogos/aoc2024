from sys import stdin

res = 0

for line in stdin:
    num = int(line)
    nums = []
    nums.append(num%10)
    for i in range(2000):
        num=(num^(num << 6))%16777216
        num=(num^(num >> 5))%16777216
        num=(num^(num << 11))%16777216
    res += num

print(res)