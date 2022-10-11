a = [1,2,3]
b = [1,2,3]

print(a == b) # True
print(a != b) # False
print(not a != b) # True

evens = [2,4,6]
evens2 = [2,4,6]
evens = evens2
print(evens == evens2) # True
print(evens is evens2) # True

# quiz
colors = ['r', 'g', 'b']
letters = colors
letters.append('z') # .append() method

print(letters, colors)
