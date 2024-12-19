with open("19.txt", "r") as f:
    towels = f.readline().replace("\n", "").split(", ")
    f.readline()
    arrangements = []
    while s:=f.readline():
        arrangements.append(s.replace("\n", ""))
    
    res = 0
    
    for arr in arrangements:
        nodes = [""]
        while len(nodes):
            node = nodes.pop()
            for piece in towels:
                if arr[len(node):len(node)+len(piece)] == piece:
                    nodes.append(node+piece)
            if node == arr:
                res += 1
                break
    print(res)