# 2D list
arr = [[0] * 4 for i in range(4)]
print(arr)

# this wont work even the result looks the same, below is creating 4 identical row, not unique to its index
arr = [[0] * 4] * 4
print(arr)