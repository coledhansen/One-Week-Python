from multiprocessing.sharedctypes import Value

# try and excpet
try: 
    num = int(input("Enter a number:\n> "))
    print(f"You entered: {num}")
except:
    raise ValueError

# multiple excepts
try:
    num = int(input("Enter an integer: "))
    print(10/num)
except ValueError:
    print("That's not an int!")
except ZeroDivisionError:
    print("Can't divide by zero!")


