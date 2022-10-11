height = int(input("What is your height (in inches)?\n> "))
weight = int(input("What is your weight (in pounds)?\n> "))

bmi = (weight*703)/(height*height)
bmi = round(bmi, 1)

# severly underweight
if bmi < 16.0:
    print(f"Your BMI of {bmi} makes you Severly Underweight")
# underweight    
elif bmi < 18.4:
    print(f"Your BMI of {bmi} makes you Underweight")
# normal
elif bmi < 24.9:
    print(f"Your BMI of {bmi} makes you Normal")
# overweight
elif bmi < 29.9:
    print(f"Your BMI of {bmi} makes you Overweight")
# moderately obese
elif bmi < 34.9:
    print(f"Your BMI of {bmi} makes you Moderately Obese")
# severly obese
elif bmi < 39.9:
    print(f"Your BMI of {bmi} makes you Severly Obese")
# morbidly obese
else:
    print(f"Your BMI of {bmi} makes you Morbidly Obese")
