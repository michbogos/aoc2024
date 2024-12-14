import re

with open("../inputs/14.txt", "r") as f:
    pat = re.compile(r"-*\d+")
    width = 101
    height = 103
    robots = []
    for line in f.readlines():
        nums = [int(num) for num in pat.findall(line)]
        robots.append(nums)
    
    for t in range(100):
        for i in range(len(robots)):
            robots[i][0] = (robots[i][0]+robots[i][2])%width
            robots[i][1] = (robots[i][1]+robots[i][3])%height
    

    mat = [[0 for _ in range(width)] for _ in range(height)]

    for r in robots:
        mat[r[1]][r[0]] += 1

    q1 = 0

    for i in range(height//2):
        for j in range(width//2):
            q1 += mat[i][j]
    q2 = 0
    for i in range(height//2+1, height):
        for j in range(width//2):
            q2 += mat[i][j]
    
    q3 = 0
    for i in range(height//2+1, height):
        for j in range(width//2+1, width):
            q3 += mat[i][j]

    q4 = 0
    for i in range(height//2):
        for j in range(width//2+1, width):
            q4 += mat[i][j]
    
    print(q1*q2*q3*q4)
