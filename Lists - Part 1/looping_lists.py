emails = [
    "jimbo@gmail.com",
    "daisy@yahoo.com",
    "otter@gmail.com",
    "maren@aol.net",
    "jessica@facebook.com"
]

# for loop
for email in emails:
    print(f"Welcome, {email}!")

print()

# while loop
idx = 0
while idx < len(emails):
    print("***SENDING EMAIL TO***")
    print(emails[idx])
    idx += 1

# quiz
colors = ["red", "orange", "yellow", "green"]
idx = len(colors) - 1
while idx >= 0:
    print(colors[idx])
    idx -= 1
