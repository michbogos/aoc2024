with open("../inputs/05.txt" , "r") as f:
    order, updates = "".join(f.readlines()).split("\n\n")
    order = [item.split("|") for item in order.split("\n")]
    s = 0
    for update in updates.split("\n"):
        nums = [num for num in update.split(",")]

        correct = True
        for order_item in order:
            try:
                if nums.index(order_item[0]) > nums.index(order_item[1]):
                    correct = False
                    break
            except ValueError:
                pass
        
        if correct:
            s += int(nums[len(nums)//2])
    
    print(s)