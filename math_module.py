# Division is decimal by default
print(5 / 2)   # 2.5

# Double slash rounds down
print(5 // 2)   # 2

# CAREFUL: most languages round towards 0 by default so negative numbers will round down
print(-3 // 2)   # -2
# A workaround for rounding towards zero is to use decimal division and then convert to int
print(int(-3 // 2))   # -1


# Modding is similar to most languages
print(10 % 3)   # 1
# except for negative values
print(-10 % 3)   # 2
# to be consistent with other languages module
import math
print(math.fmod(-10, 3))  # -1


# more math helpers
print(math.floor(3 / 2))  # round down
print(math.ceil(3 / 2))   # round up
print(math.sqrt(2))
print(math.pow(2, 3))


# max / min int
float("inf")
float("-inf")
# python numbers are infinite so they never overflow
print(math.pow(2, 200))

print(math.pow(2, 200) < float("inf"))
