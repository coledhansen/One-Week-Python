evens_list = [2,4,6,8]
    # python will iterate over each item in list
    # decreases performance
evens_set = {2,4,6,8}
    # more efficient
    # involves hashing

print(
    8 in evens_list,
    8 in evens_set
)

states = [
    'CA',
    'AZ',
    'CA',
    'AK',
    'HI',
    'CA'
]

# turn into set
states = set(states)
print(states)
print(type(states))

# turn back into list
states = list(states)
print(type(states))

### unordered
### mutable (set elements are immutable)
### no duplicates are allowed
