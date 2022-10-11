msg = '   asdf...'

# can pass in values that are not default for strip() method
print(msg.strip())
print(msg.strip("."))
print(msg.strip(". "))

# laugh() function
def laugh(intensity = 10):
    print("HA" * intensity)

# check result
laugh()

# back to slugify()
def slugify(txt, sep="-"):
    return str(txt).strip().replace(" ", sep).lower()

print(slugify("hello haha what's up", "_")) # provides custom separator

# quiz
def divide (x=1,y=4):
  return x/y

print(divide(2)) # 0.5
print(divide()) # 0.25
print(divide(1,5)) # 0.2
