# GLOBAL scope
movie = 'Amadeus'
def reviews():
    print(movie)
    def inner():
        print(movie)
    inner()
reviews() # everything has access to the movie variable    

# example
animal = "Lemur"
print("OUTSIDE OF FUNCTION: ", animal)

def func():
    print("INSIDE FUNC: ", animal)
func()

