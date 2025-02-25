#Exercises: Day 9
#Exercises: Level 1
#1
# user_input = int(input("Enter your age: "))
# if user_input < 18:
#     difference = 18 - user_input
#     print(f"You need {difference} more years to learn to drive")
# elif user_input >= 18:
#     print("You are old enough to drive")

#2
# my_age = 20
# your_age = int(input("Enter your age: "))
# if your_age < my_age:
#     subtract = my_age - your_age
#     print(f"You are {subtract} years younger than me.")
# elif your_age > my_age:
#     subtract1 = your_age - my_age
#     print(f"You are {subtract1} years older than me.")
# else:
#     print("We are the same age")

#3
# a = input("Enter number one: ")
# b = input("Enter number two: ")
# if a > b:
#     print(f"{a} is greater than {b}")
# elif a < b:
#     print(f"{a} is smaller than {b}")
# else:
#     print(f"{a} is equal to {b}")


#Exercises: Level 2
#1
# score = int(input("Enter your score: "))
# if score >= 80 and score == 100:
#     print("A")
# elif score >= 70 and score <= 89:
#     print("B")
# elif score >= 60 and score <= 69:
#     print("C")
# elif score >= 50 and score <= 59:
#     print("D")
# elif score >= 0 and score <= 49:
#     print("F")
# else:
#     print("Invalid score")

#2
# month = input("Enter month: ")
# if month in ["September", "October", "November"]:
#     print("The season is Autumn")
# elif month in ["December", "January", "February"]:
#     print("The season is Winter")
# elif month in ["March", "April", "May"]:
#     print("The season is Spring")
# elif month in ["June", "July", "August"]:
#     print("The season is Summer")
# else:
#     print("Invaild input.")

#3
# fruits = ["banana", "orange", "mango", "lemon"]
# fruit = input("Enter fruit: ")
# if fruit in fruits:
#     print("That fruit already exist in the list.")
# elif fruit not in fruits:
#     fruits.append(fruit)
#     print(f"New list {fruits}")
# else:
#     print("Invalid input")

#Exercises: Level 3
#1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
print(person["skills"])

skills = person["skills"]

print(skills[len(skills)//2])

#2
print("Python" in skills)

#3
if skills == ["Javascript", "React"]:
    print("He is a front end developer")
elif skills == ["Node", "Python", "MongoDB"]:
    print("He is a backend developer")
elif skills == ["React", "Node", "MonogoDB"]:
    print("He is a fullstack developer")
else:
    print("unknown title")

#4
is_married = person["is_married"]
country = person["country"]

if person is is_married and person == "Finland":
    print(f"Asabeneh Yetayeh lives in {country}. He is married.")