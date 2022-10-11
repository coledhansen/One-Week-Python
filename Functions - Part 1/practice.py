### is_even() function
# first way
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# second way
def is_even(num):
    if num % 2 == 0:
        return True
    return False

# third way
def is_even(num):
    return num % 2 ==0

print(is_even(4))

### slugify() function
## .lower(), .strip(), .replace()

def slugify(txt):
    return str(txt).strip().replace(" ", "-").lower()

print(slugify("hello world I LOVE YOU  "))

### count_vowels() function
## .find()?

def count_vowels(txt):
    count = 0
    for char in txt:
        if char in "aeiou":
            count += 1
    return count

print(count_vowels("hello world"))
print(count_vowels("sss"))