import heapq

mat1 = [["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["", "0", "A"]]

mat2 = [["", "^", "A"],
        ["<","v", ">"]]

# def find_shortest(cs, ce, mat):
#     heap = []
#     start = (0, 0)
#     end = (0, 0)
#     next = []
#     dist = [[10e10 for i in range(len(mat[0]))] for j in range(len(mat))]
#     for i in range(len(mat)):
#         for j in range(len(mat[i])):
#             if mat[i][j] == cs:
#                 start = (i, j)
#             if mat[i][j] == ce:
#                 end = (i, j)
    
    # heapq.heappush()

cur1 = [3, 2]
cur2 = [0, 2]
cur3 = [0, 2]

def findcode(code, mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == code:
                return [i, j]

with open("21.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

    button_pos1 = {k:findcode(k, mat1) for k in "0123456789A"}
    button_pos2 = {k:findcode(k, mat2) for k in "^<>vA"}

    for codes in lines:
        commands = ""
        for code in codes:
            nxt = button_pos1[code]
            dx = nxt[1]-cur1[1]
            dy = nxt[0]-cur1[0]
            if mat1[cur1[0]][cur1[1]] == "0" and code == "1":
                commands += "^<"
                cur1[0] -= 1
                cur1[1] -= 1
            elif mat1[cur1[0]][cur1[1]] == "1" and code == "0":
                commands += ">v"
                cur1[0] += 1
                cur1[1] += 1
            else:
                if dx > 0:
                    commands += ">"*abs(dx)
                if dx < 0:
                    commands += "<"*abs(dx)
                if dy > 0:
                    commands += "v"*abs(dy)
                if dy < 0:
                    commands += "^"*abs(dy)
            commands += "A"
            cur1 = nxt

        commands2 = ""
        
        # print(commands)
        
        for code in list(commands):
            nxt = button_pos2[code]
            dx = nxt[1]-cur2[1]
            dy = nxt[0]-cur2[0]
            if mat2[cur2[0]][cur2[1]] == "^" and code == "<":
                commands2 += "v<"
                cur2[0] += 1
                cur2[1] -= 1
            elif mat2[cur2[0]][cur2[1]] == "<" and code == "^":
                commands2 += ">^"
                cur2[0] -= 1
                cur2[1] += 1
            else:
                if dx > 0:
                    commands2 += ">"*abs(dx)
                if dx < 0:
                    commands2 += "<"*abs(dx)
                if dy > 0:
                    commands2 += "v"*abs(dy)
                if dy < 0:
                    commands2 += "^"*abs(dy)
            commands2 += "A"
            cur2 = nxt
        
        # print(commands2)

        commands3 = ""
        
        for code in list(commands2):
            nxt = button_pos2[code]
            dx = nxt[1]-cur3[1]
            dy = nxt[0]-cur3[0]
            if mat2[cur3[0]][cur3[1]] == "^" and code == "<":
                commands3 += "v<"
                cur3[0] += 1
                cur3[1] -= 1
            elif mat2[cur3[0]][cur3[1]] == "<" and code == "^":
                commands3 += ">^"
                cur3[0] -= 1
                cur3[1] += 1
            else:
                if dx > 0:
                    commands3 += ">"*abs(dx)
                if dx < 0:
                    commands3 += "<"*abs(dx)
                if dy > 0:
                    commands3 += "v"*abs(dy)
                if dy < 0:
                    commands3 += "^"*abs(dy)
            commands3 += "A"
            cur3 = nxt
        
        print(commands3, len(commands3))
        


