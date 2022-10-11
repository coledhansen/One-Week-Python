first_name = input("What is your first name?\n> ")
last_name = input("What is your last name?\n> ")

full_name = first_name + " " + last_name
# print(full_name)

print("*************")

if len(full_name) > 12:
    print(f"{full_name} is longer than the average American name.")
elif len(full_name) < 12:
    print(f"{full_name} is shorter than the average American name.")
elif len(full_name) == 12:
    print(f"{full_name} is as long as the average American name.")

print("*************")
