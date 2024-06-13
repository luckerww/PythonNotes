# HashSet
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

# search within the set using 'in' without a function.
print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)


# list to set
print(set([1, 2, 3]))
# Set comprehension (similar to list comprehension)
mySet = {i for i in range(5)}
print(mySet)