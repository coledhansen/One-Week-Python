# lbyl - look before you loop
year = input("Enter a year:\n> ")
if year.isnumeric():
    year = int(year)
else: year = 2025

# eafp - easier to ask for forgiveness than permission
try:
    year = int(input("Enter a year:\n> "))
except ValueError:
    year = 2025
