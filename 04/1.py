with open("../inputs/04.txt", "r") as f:
    s = 0
    mat = [line for line in f.readlines()]
    #row
    for i in range(len(mat)):
        for j in range(len(mat[i])-3):
            if "".join(list([mat[i][j+k] for k in range(4)])) == "XMAS":
                s += 1
    #row reverse
    for i in range(len(mat)):
        for j in range(3, len(mat[i])):
            if "".join(list([mat[i][j-k] for k in range(4)])) == "XMAS":
                s += 1
    
    #coulmn
    for i in range(len(mat)-3):
        for j in range(len(mat[i])):
            if "".join(list([mat[i+k][j] for k in range(4)])) == "XMAS":
                s += 1
    
    #coulmn reverse
    for i in range(3, len(mat)):
        for j in range(len(mat[i])):
            if "".join(list([mat[i-k][j] for k in range(4)])) == "XMAS":
                s += 1
    #diagonal 1
    for i in range(len(mat)-3):
        for j in range(len(mat[i])-3):
            if "".join(list([mat[i+k][j+k] for k in range(4)])) == "XMAS":
                s += 1
    #diagonal 2
    for i in range(3, len(mat)):
        for j in range(len(mat[i])-3):
            if "".join(list([mat[i-k][j+k] for k in range(4)])) == "XMAS":
                s += 1
    
    #diagonal 3
    for i in range(3, len(mat)):
        for j in range(3, len(mat[i])):
            if "".join(list([mat[i-k][j-k] for k in range(4)])) == "XMAS":
                s += 1
    
    #diagonal 4
    for i in range(len(mat)-3):
        for j in range(3, len(mat[i])):
            if "".join(list([mat[i+k][j-k] for k in range(4)])) == "XMAS":
                s += 1
    
    print(s)
            