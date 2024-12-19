with open("../inputs/19.txt", "r") as f:
    towels = f.readline().replace("\n", "").split(", ")
    f.readline()
    arrangements = []
    while s:=f.readline():
        arrangements.append(s.replace("\n", ""))
    
    res = 0
    
    for i, arr in enumerate(arrangements):
        ways = [0 for _ in range(len(arr)+1)]
        ways[0] = 1
        for pat in towels:
            if arr[0:len(pat)] == pat:
                ways[len(pat)] += 1

        for idx in range(len(arr)):
            for pat in towels:
                if idx+len(pat) <= len(arr):
                    if arr[idx:idx+len(pat)] == pat:
                        ways[idx+len(pat)] += ways[idx]
            
        res += ways[len(arr)]
    print(res//2)