def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean

monday_temperatures = [8.6, 9.1, 9.9]
student_grades = {"Marry": 9.1, "Sim":8.8, "John":7.5}

print(mean(monday_temperatures))

##
def string_checker(string):
    if len(string) >= 8:
        return True
    else: return False

##
def temp_checker(temp):
    if temp >= 8:
        return 'Warm'
    else: return 'Cold'

##
def temp_reader(temp):
    if temp > 25:
        return 'Hot'
    elif temp >= 15 and temp <= 25:
        return 'Warm'
    else: return 'Cold'

##
def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else: return "Cold"

user_input = float(input("Enter temperature:")) # convert to float
print(weather_condition(user_input))
