stuff = ["string", True, 3.4, None]
print(stuff)

stuff.append([3, 4])
print(stuff)

couples = [
    ["Beyonce", "Jay-Z"],
    ["Johnny", "June"],
    ["John", "Yoko"],
    ["Will", "Jada"]
]

print(len(couples))
print(couples[1][0])

for couple in couples:
    for person in couple:
        print(f"Sending invite to: {person}")

# two dimensional array
[
    ['X', '0', 'X'],
    ['0', '0', 'X'],
    ['X', 'X', '0']
]

