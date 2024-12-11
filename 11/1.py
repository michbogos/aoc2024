with open("../inputs/11.txt", "r") as f:
    stones = [int(stone) for stone in f.readline().split(" ")]
    for i in range(25):
        for i in range(len(stones)):
            if stones[i] == 0:
                stones[i] = 1
            elif len(str(stones[i])) % 2 == 0:
                s = str(stones[i])
                stones[i]=int(s[0:len(s)//2])
                stones.append(int(s[len(s)//2: len(s)]))
            else:
                stones[i] = stones[i]*2024
    print(len(stones))