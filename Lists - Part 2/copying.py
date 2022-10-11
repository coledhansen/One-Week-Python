# just pointing variables at each other DOES NOT copy
## use .copy()

race_results = ['bill', 'ted', 'tammy', 'jimbo', 'billybob', 'pierre']

r2 = race_results.copy()
print(r2)

# can check with id()
print(r2 is race_results) # False - different id()
print(r2 == race_results) # True - same underlying contents

## .deepcopy()
import copy
list1 = [2,9,['a','b'],7]

list2 = list1.copy()
print(list2)

list2 = copy.deepcopy(list1)
print(list2)
