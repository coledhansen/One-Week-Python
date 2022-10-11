def greet(msg, person):
    print(f"{msg}, {person}!")

greet("Hello", "Cole")

def greet_v2(person, msg="Hi"): # ordering parameters to work, person is required
    print(f"{msg}, {person}!")

greet_v2("Tonya")

def greet_v3(person="stranger", msg="Hi"):
    print(f"{msg}, {person}!")

greet_v3()
greet_v3("Bye")
    # order fills left to right
    # python fills "stranger" with "Bye" then defaults to "Hi"
