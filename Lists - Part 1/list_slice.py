string = 'superduper'
print(string[3:7]) # 3 up until 7 excluding

waitlist = ['juan', 'aria', 'amir', 'rosa', 'colt', 'charlie', 'drew', 'emi']
# alternate syntax
print(waitlist[5:])
print(waitlist[:5])

# every other element from full list
print(waitlist[::2])

print(waitlist[1:7:2])

# updating with slice
nums = [4,5,6,7]
print(nums[1:3]) # 5, 6
nums[1:3] = ['a', 'b']
print(nums)

nums = [4,5,6,7]
nums[1:3] = ['a', 'b', 'c', 'd']
print(nums[1:5])

# str object does not support item assignment
    # lists do
