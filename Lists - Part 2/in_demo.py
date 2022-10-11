a = [1,2,3]
b = [4,5,6]

print(4 in b) # True
print(7 in b) # False

# example
flavors = [
    "chocolate",
    "vanilla",
    "lemon",
    "strawberry"
]

response = input("What flavor would you like?\n> ")

while response.lower() not in flavors:
    response = input("I don't know that flavor! Try again:\n> ")

print()
print(f"OK, {response} ice cream coming right up!")