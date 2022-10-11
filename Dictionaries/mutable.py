d1 = {1: 'one'}

d2 = d1
print(
    id(d1), id(d2)
    # returns same result (same pointer)
)

print(d1 is d2) # True

d3 = d1.copy()
print(d3 is d1) # False !
