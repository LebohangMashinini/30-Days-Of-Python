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
score = int(input("Enter your score: "))
if score >= 80 and score == 100:
    print("A")
elif score >= 70 and score <= 89:
    print("B")
elif score >= 60 and score <= 69:
    print("C")
elif score >= 50 and score <= 59:
    print("D")
elif score >= 0 and score <= 49:
    print("F")
else:
    print("Invalid score")

#2