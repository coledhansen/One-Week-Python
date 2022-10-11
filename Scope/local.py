# LOCAL scope
def cube(num):
    answer = num ** 3 # variable is scoped to that function
    print(answer)

def zoo():
    animal = "Harlequin Shrimp"
    print("INSIDE ZOO FUNCTION: ", animal)

zoo()
# error
# print(animal) - can't find it because it is locally scoped inside zoo() function
