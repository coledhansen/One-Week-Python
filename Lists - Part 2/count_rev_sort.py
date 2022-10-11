## .count()
lando_2021_results = [4,3,5,8,3,5,5,5,3,4,14,10,2,7,7,8,10,10,9,10,7]

print(lando_2021_results.count(1)) # 0
print(lando_2021_results.count(3)) # 3!

## .reverse()
drivers = ['yuki', 'charles', 'lando']
drivers.reverse()
print("List now: " + str(drivers))

## .sort()
nums = [4,5,12,8,-23,342,6,5,0]
nums.sort()
print("List now: " + str(nums))

# reverse parameter
nums = [4,5,12,8,-23,342,6,5,0]
nums.sort(reverse = True)
print("List now: " + str(nums))

colors = ['red', 'orange', 'purple', 'green']
colors.sort()
colors.append("Z")
colors.sort()
print("List now: " + str(colors)) # watch alphabetical ordering
