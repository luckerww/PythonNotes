# Sorting
arr = [1, 3, 2, 5, 6, 7, 10]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

arr = ['bob', 'tim', 'miller', 'kobe']
arr.sort()
print(arr)
# Custom sort (by length of string) lambda
arr.sort(key=lambda x: len(x))
print(arr)
