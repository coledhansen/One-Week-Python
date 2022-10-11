evens = {2,4,6,8}

## .add()
evens.add(10)
evens.add(12)
print(evens)
    # {2, 4, 6, 8, 12}

evens.add(-4)
    # what order?
print(evens)
    # {2, 4, 6, 8, 12, -4}

## .remove()
evens.add(7)
print(evens)

evens.remove(7) # tells Python to remove element from set
evens.remove(-4)
print(evens)

## .discard()
    # won't throw an error if value is not present
evens.discard(3) # doesn't exist
print(evens)

## .clear()
    # empties out set entirely

# comparison
a = {1,2,3}
b = {1,2,3}
print(a is b) # False - different contains in memory
print(a == b) # True - contents are identical

print(2 in a) # True
print(5 in a) # False

# iterate
for num in a:
    print(num)
    # 1
    # 2
    # 3
