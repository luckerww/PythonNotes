#  Arrays (called lists in python
arr = [1, 2, 3]
print(arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1,7)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)



# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Careful: -1 is not out of bounds,
# -1 in python is the last value
arr = [1,2,3]
print(arr[-1])

# -2 in python is the second to the last value, etc.
arr = [1,2,3]
print(arr[-2])


# Sublists (aka slicing)
arr = [1,2,3,4]
print(arr[1:3])

# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

# Loop through arrays
nums = [1, 2, 3]
# using index
for i in range(len(nums)):
    print(nums[i])
# without index
for n in nums:
    print(n)
# With index and value
for i, n in enumerate(nums):
    print(i, n)

# Loop through multiple arrays simultaneously
# with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)



