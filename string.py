# Strings are similar to arrays
s = "abc"
print(s[0:2])

# But strings are immutable
    # s[0] = "A" will result an error

s += "def"
print(s)


# Valid numeric strings can be converted
print(int("123") + int("123"))

# And numbers can be converted to strings too
print(str(123) + str(123))


# in rare cases you may need the ASCII value of a char
print(ord("a"))
print(ord("b"))

# combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print(" ".join(strings))