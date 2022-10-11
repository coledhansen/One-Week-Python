def add_thrice(val, lst = []):
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst

print(add_thrice(7, [1,2,3]))
print(add_thrice(99))
print(add_thrice(0)) # doesn't create empty list with zeros, adds onto the 99s from before

## how to fix this issue?
def add_thrice(val, lst = None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst

print(add_thrice(99))
print(add_thrice(0))
    # now works
    # list was emptied and now contains only 3 zeros

# problem only involves MUTABLE objects
