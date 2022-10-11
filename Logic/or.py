fav_team = input("What is your favorite soccer team?\n> ")

if fav_team == 'Manchester City' or fav_team == 'Manchester United':
    print("You must live in Manchester.")
    print()
else:
    print("Hmm, you must not be a Manc.")
    print()

day = input("What day of the week is it?\n> ")
if day == 'Saturday' or day == 'Sunday':
    print("It's the weekend!")
    print()
else:
    print("Ugh - it's a work day.")
    print()

age_under = 5
age_over = 65

age = int(input("What is your age?\n> "))
if age <= age_under or age >= age_over:
    print("You get in for free!")
else:
    print("Sorry - you have to pay if you're not a toddler or senior citizen.")
    print()
    