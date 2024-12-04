with open("../inputs/04.txt", "r") as f:
    s = 0
    mat = [line for line in f.readlines()]
    #diagonal 1
    for rot in range(4):
        mat = list(zip(*mat[::-1]))
        for i in range(len(mat)-2):
            for j in range(len(mat[i])-2):
                if "".join([mat[i+k][j+k] for k in range(3)]) == "MAS" and "".join([mat[i+2-k][j+k] for k in range(3)]) == "MAS":
                    s += 1

    print(s)
            