animal = 'Nudibranch'

def outer():
    animal = "Echnida"
    def inner():
        print("FROM INNER FUNC: ", animal)
    print("FROM OUTER FUNC: ", animal)
    inner()

print("OUTSIDE OF FUNCTIONS: ", animal)
outer()

# outer() # locally scope
# print(animal) # global scope

# ^ Built-In
# | Global
# | Enclosing
# | Local
