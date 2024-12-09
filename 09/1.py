with open("../inputs/09.txt", "r") as f:
    files = "".join(f.readlines()).replace("\n", "")
    size = sum([int(c) for c in files])
    disk = [-1 for _ in range(size)]
    pointer = 0
    fileid = 0
    for i, c in enumerate(files):
        if i%2 == 0:
            length = int(c)
            for ll in range(length):
                disk[pointer+ll] = fileid
            pointer += length
            fileid += 1
        else:
            length = int(c)
            pointer += length
    
    front = 0
    back = len(disk)-1
    while back != front:
        if disk[front] == -1 and disk[back] != -1:
            disk[front] = disk[back]
            disk[back] = -1
            back -= 1
            front += 1
        if disk[front] != -1:
            front += 1
        if disk[back] == -1:
            back -= 1
    
    res = 0

    for i, num in enumerate(disk):
        if num != -1:
            res += i*num
    
    print(res)