from itertools import count

### python built-in args
## min
print(min(1, 2)) # 1
## max
print(max(3, 4)) # 4

## len()
print(len("hello"))
    # one argument passed into len()

def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total/len(args)

print(
    average(1,2,3,4,5), # 3.0
    average(10,1) # 5.5
)

def count_stuff(*args):
    return args
print(count_stuff(1,5,4,6,7,1))
    # returns TUPLE
    # (1, 5, 4, 6, 7, 1)

def count_stuff_2(*args):
    return f"You passed me {len(args)} arguments!"
print(count_stuff_2(1,5,4,6,7,1))
    # You passed me 6 arguments!

## does NOT need to be args keyword
def count_stuff_2(*things):
    return f"You passed me {len(things)} arguments!"
print(count_stuff_2(True, False, True, 7, 3.0, 'hello', 'goodbye'))
    # You passed me 7 arguments!

def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total 
print(sum(1,2,3,4,5)) # 15
print(sum(4,6)) # 10

def silly(first, second, *others):
    return f"First is: {first}, Second is: {second}, Others is: {others}"
    
print(silly('hello', 'goodbye', 'see ya later', 'alligator'))
    # *others argument is returned as a tuple of two strings

def silly_goose(num, *args):
  return args
print(silly_goose(1,2,3,4,5))

def login(first, *args):
  return "does nothing"
print(
    login("Charlie"),
    login("Debbie", "Timmy"),
    login("Debbie", "Timmy", "Annie", "Tommy")
)

