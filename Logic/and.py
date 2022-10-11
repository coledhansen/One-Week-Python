print('a' == 'a' and 1 < 5) # both are true

age = 18
print(age > 10 and age < 21)

print(3 < 4 and 3 != 3) # false since one side is false

# logical and
age = int(input("What is your age?\n> "))

if age > 18 and age < 21: # both have to be true to run
    print("You are allowed in the venue.")
elif age > 21:
    print("You are allowed to enter and drink at the venue")
else: print("You are not allowed in the venue.")
