print(not False) # True
print(not True) # False

print(not not False) # False (lol)

age = 7
print(not age < 18)

# in practice
temp = -19
print(not temp <= 0)

# age calculator
year = input("What year were you born in?\n> ")

if year.isnumeric():
    year = int(year)
    print(f"You were born {2022-year} years ago.")
else:
    year = input("That is not a valid year. Try again please. What year were you born in?\n> ")
    year = int(year)
    print(f"You were born {2022-year} years ago.")
