d1 = {'a': 1, 'b': 2}
stuff = {
    'c': 3,
    'd': 4,
    'e': 5,
    'a': 'apple'
}

d1.update(stuff)
print(d1)

## double star **
dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}
dict3 = {**dict1, **dict2}
print(dict3)

## dict union |
dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}
dict3 = dict1 | dict2
print(dict3)
