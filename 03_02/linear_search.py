def linear_search(data, target):
    a = 1
    for i in data:
        if target == i:
            return a
            break
        else:
            a +=1
            continue
    return -1


data = [4, 5, 2, 7, 1, 8]
target = 1
result = linear_search(data, target)
if result == -1:
    print("Item not found.")
else:
    print(f"Item found at position {result}.")
