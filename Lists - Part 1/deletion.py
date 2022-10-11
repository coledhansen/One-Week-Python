## .clear()
langs = ['Python', 'C', 'JS', 'C']
langs.clear() 
print(langs) # empty list

## .remove()
langs = ['Python', 'C', 'JS', 'C']
langs.remove('C')
print(langs) # removes only FIRST match
    # remove also needs exact match specified

nums = [2,4,6,8,2,4]
nums.remove(4)
print(nums) # second 4 is still there after .remove()

## .pop()
# most common way
order = ['first', 'second', 'third']
print(order.pop()) # third

print(langs.pop(0)) # Python
print(langs) # left with two values in list

letters = ['a', 'z', 'q', 't']
del letters[0] # syntax for del statement
    # doesn't return anything automatically
print(letters)
    # list now has 3 elements

nums = [1,2,3,4,5,6,7,8,9]
del nums[::2]
print(nums)
    # only evens

# f1 example
drivers = ['esteban', 'fernando','lando', 'pierre', 'yuki', 'daniel']
mclaren = ['daniel']

norris = drivers.pop(2)

mclaren.append(norris)
print(mclaren)
