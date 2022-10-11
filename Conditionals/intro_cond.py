age = int(
    input("What is your age in years?\n> ")
)

# first way
if age >= 21:
    print("Bottoms up!")
else: print("Kick it, bud.")

# second way
if age >= 21:
    print("Bottoms up!")
print("Kick it, bud.")
    # lack of indentation corresponds to False
    # if True, both are printed
