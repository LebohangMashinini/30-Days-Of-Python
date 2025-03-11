#Exercises: Day 11
#Exercises: Level 1
#1
# def add_two_numbers(x, y):
#     add = x + y
#     return add

# #2
# pi = 3.14
# def area_of_circle(radius):
#     area = pi * radius * radius
#     return area

#3
def add_all_nums(*numbers):
    if not all(isinstance(number, (int, float))for number in numbers):
        return "All numbers must be numbers"
    return sum(numbers)
print(add_all_nums(2, 2, 2, 2))

#4
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(5))

#5
def check_season(month):
    if month in ["September", "October" "November"]:
        return "Spring"
    elif month in ["December", "January", "February"]:
        return "Summer"
    elif month in ["March", "April", "May"]:
        return "Autumn"
    elif month in ["June", "July", "August"]:
        return "Winter"
print(check_season("June"))