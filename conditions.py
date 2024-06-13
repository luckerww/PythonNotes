age = int(input("what's your age?\n>>>: "))

if age >= 72:
    print("You shouldnt drink.")
elif age >= 21:
    print("You're legal to drink!")
elif age >= 18: #otherwise if
    print("you're not there yet.")
else: #everything else
    print("You're not legal to drink!")