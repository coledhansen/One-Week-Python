## **kwargs
# two stars in front of a parameter in a python def tells python
# that it should create a dictionary of all key-value pairs

def demo(**kwargs):
    return kwargs

print(demo(color = "red", age = 12))
    # color and age turned into keys
    # "red" and 12 turned into valuefs

def print_ages(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} is {v} years old.")

print(print_ages(max=67, sue=59, kim=14))
