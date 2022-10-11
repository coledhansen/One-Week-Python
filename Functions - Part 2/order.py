## importance of order
# parameters -> *args -> default parameters -> **kwargs
def display_info(person, status = "single"):
    print(f"person is: {person}")
    print(f"status is: {status}")
# !!! - if try to switch person and status parameters, error will follow

def display_info(person, *args, status = "single", **kwargs):
    print(f"person is: {person}")
    print(f"status is: {status}")
    print(f"args is: {args}")
    print(f"kwargs is: {kwargs}")

print(display_info("colt", 4,5,6,7,8, status = "married", age = 87, mood = "thrilled"))

