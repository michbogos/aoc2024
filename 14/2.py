import re

with open("../inputs/14.txt", "r") as f:
    res = 0
    pat = re.compile(r"-*\d+")
    width = 101
    height = 103
    robots = []
    for line in f.readlines():
        nums = [int(num) for num in pat.findall(line)]
        robots.append(nums)
    
    frame = 0
    while True:
        frame += 1
        print(frame)
        for i in range(len(robots)):
            robots[i][0] = (robots[i][0]+robots[i][2])%width
            robots[i][1] = (robots[i][1]+robots[i][3])%height
    

        mat = [[0 for _ in range(width)] for _ in range(height)]

        for r in robots:
            mat[r[1]][r[0]] += 1
        
        for i in range(0, height-7, 7):
            for j in range(0, width-7, 7):
                s = 0
                for x in range(7):
                    for y in range(7):
                        s += mat[i+y][j+x]
                if s >= 49:
                    print("Easter egg:", frame)
                    exit()
        

    
