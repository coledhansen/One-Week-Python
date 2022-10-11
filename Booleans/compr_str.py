print('a' < 'w')
print('A' < 'w')
print('aaa' < 'AAA')
print('A' < 'a')

# ord() function
print(ord('a')) # 97
print(ord('A')) # 65

str1 = 'ABC'
str2 = 'AbC'
str3 = 'ABc'

print('100' < '9') # python looks at ord() of each and determines True
