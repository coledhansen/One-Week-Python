color = 'green'
color = 'blue'

if color == 'green':
    print("Beginner Ski Run")
elif color == 'blue':
    print("Intermediate Ski Run")
elif color == 'black':
    print("Expert Ski Run")

# indentation is key to show Python what to run

num = 3
if num > 0:
    print("FROM THE IF") 
elif num == 3:
    print("From ELIF 1") # elif will only run if nothing before them in the conditional is true
elif num < 10:
    print("FROM ELIF 2")
