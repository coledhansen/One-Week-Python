## .append()
packers_wr = ['Cobb', 'Lazard', 'Adams']
packers_wr.append('Watson')
print(packers_wr)
    # ['Cobb', 'Lazard', 'Dobbs', 'Watson']

waitlist = ['juan', 'aria', 'amir']
waitlist.append('joe')
print(waitlist)

## .extend()
car_class = ['a', 's', 'r']
car_class.extend('123')
print(car_class) # iterates over 1, then 2, then 3
print(len(car_class)) # 6

# another example
added_party = ['charlie', 'drew', 'emi']
waitlist.extend(added_party)
print(waitlist) # should be 7 people total

# another example
nums = [2,4,6]
extension = [1,3]
nums.extend(extension)
print(nums) # iterates through list as individual values
