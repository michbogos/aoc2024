with open("../inputs/02.txt", "r") as f:
    s = 0
    for line in f.readlines():
        nums = line.split(" ")
        inc = True
        dec = True
        for a, b in zip(nums, nums[1:]):
            if not (int(b)-int(a) > 0 and int(b)-int(a) < 4):
                inc = False
                break
        for a, b in zip(nums, nums[1:]):
            if not (int(a)-int(b) > 0 and int(a)-int(b) < 4):
                dec = False
        if inc or dec:
            s += 1
    print(s)
