animal = 'Walrus'

def outer():
    global animal
    animal = "Spider Crab"
    print(animal)

outer()
print(animal)

# another example
def double_score():
    global score
    score = score * 2
    print(score)

score = 100
double_score()

# quiz
color = "purple"
 
def my_func():
   global color
   color = "green"
 
print(color)
my_func()
print(color)
