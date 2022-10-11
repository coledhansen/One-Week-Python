def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total 

print(sum(3,4,5,6,7,1,23,3))

nums = [1,2,3,4,5,6,7,8]
# print(sum(nums)) 
    # error not set up to process list

print(sum(*nums))
    # runs
    # * operator is telling python to process each element

## reminder
d1 = {1:'one', 2:'two'}
d1 = {**d1, 3:'three'} # appending key-value pair to dict
print(d1)
