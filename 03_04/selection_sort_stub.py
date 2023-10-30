def selection_sort(xs):
    start = 0
    min_index = 0
    while start < len(xs):
        for i in range(start, len(xs)):
            if xs[i] < xs[min_index]:
                min_index = i
        min_val = xs[min_index]
        start_val = xs[start]
        xs[start] = min_val
        xs[min_index] = start_val
        start +=1
        min_index = start
    


xs = [3, 2, 1, 5, 4]
print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check  a list is sorted
# without relying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))