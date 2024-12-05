with open("../inputs/05.txt" , "r") as f:
    order, updates = "".join(f.readlines()).split("\n\n")
    order = [item.split("|") for item in order.split("\n")]
    s = 0
    for update in updates.split("\n"):
        nums = [num for num in update.split(",")]

        do = True
        wrong = False
        while do:
            corrected = False
            for order_item in order:
                try:
                    if (idx1:=nums.index(order_item[0])) > (idx2:=nums.index(order_item[1])):
                        corrected = True
                        wrong = True
                        tmp = nums[idx1]
                        nums[idx1] = nums[idx2]
                        nums[idx2] = tmp
    
                except ValueError:
                    pass
            do = corrected
        
        if wrong:
            s += int(nums[len(nums)//2])
    
    print(s)