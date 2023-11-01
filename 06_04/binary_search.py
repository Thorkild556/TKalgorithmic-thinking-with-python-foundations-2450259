import random





def binary_search(data, target):
    data.sort()
    low = 0
    high = len(data) - 1
    if target == data[high]:
        return high
    elif target == data[low]:
        return low
    while low <= high:
        half = low + high // 2
        if target == data[half]:
            return half
        elif target < data[half]:
            high = half
        elif target > data[half]:
            low = half



n = 10
max_val = 100
data = [random.randint(1, max_val) for i in range(n)]
data.sort()
print("Data:", data)
target = data[4]
target_pos = binary_search(data, target)
if target_pos == -1:
    print("Your target value is not in the list.")
else:
    print("You target value has been found at index", target_pos)
