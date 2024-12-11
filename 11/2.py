from collections import defaultdict
import sys

with open("../inputs/11.txt", "r") as f:
    sys.set_int_max_str_digits(10**5)
    stones = defaultdict(int)
    for s in [int(stone) for stone in f.readline().split(" ")]:
        stones[s] = 1
    new = defaultdict(int)
    for i in range(75):
        new.clear()
        for stone in list(stones.keys()):
            if stones[stone] > 0:
                s = str(stone)
                if stone == 0:
                    new[1] += stones[0]
                    new[0] -= stones[0]
                elif len(s) % 2 == 0:
                    new[int(s[0:len(s)//2])] += stones[stone]
                    new[int(s[len(s)//2:len(s)])] += stones[stone]
                    new[stone] -= stones[stone]
                else:
                    new[stone*2024] += stones[stone]
                    new[stone] -= stones[stone]
        for k, v in new.items():
            stones[k] += v
    print(sum([stones[stone] for stone in stones if stones[stone] > 0]))