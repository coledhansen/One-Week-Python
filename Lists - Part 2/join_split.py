# .split()
birthday = "03/27/2020".split("/")
print(birthday) # becomes list

full_name = "Teddy Richard Smith Jr.".split(" ")
print(full_name)

num_seq = "3...4...5".split(".")
print(num_seq) # ['3', '', '', '4', '', '', '5']

num_seq = "3...4...5".split("...")
print(num_seq) # ['3', '4', '5']

# .join()
fruits = ["Apple", "Kiwi", "Pear"]
print(" ".join(fruits)) # Apple Kiwi Pear
print("!!!".join(fruits)) # Apple!!!Kiwi!!!Pear

letters = ["M", "A", "S", "H"]
print("*".join(letters))

aretha = ['R','E','S','P','E','C','T']
print("-".join(aretha))

user = ["Joe", "Bucky", 42]
first, last, age = user
print(first, last, age)

color = [255,43,19]
red, green, blue = color # assignment
print(red, green, blue) # printing output
