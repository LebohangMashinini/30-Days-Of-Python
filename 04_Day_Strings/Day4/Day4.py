#Exercises Day 4
#1

# first = "Thirty"
# second = "Days"
# third = "Of"
# forth = "Python"

# print(first + second + third + forth)

# #2
# a = "Coding"
# b = "For"
# c = "All"

# print(a + b + c)

# #3
# company = "Coding For All"

# #4
# print(company)
 
# #5
# print(len(company))

# #6
# print(company.upper())

# #7
# print(company.lower())

# #8
# print(f"Capitalize: {company.capitalize()}")
# print(f"Title: {company.title()}")
# print(f"Swapcase: {company.swapcase()}")

# #9
# sentence = "Coding For All"
# print(sentence[7:])

# #10
# sentence1 = "Coding For All"
# ind = sentence1.index("Coding")
# find = sentence1.find("Coding")

# #11
# sentence2 = "Coding For All"
# x = sentence2.replace("Coding", "Python")
# print(x)

#12
# sentence3 = "Python for Everyone"
# y = sentence3.replace("for Everyone", "for All")
# print(y)

# #13
# string = "Coding For All"
# z = string.split(" ")
# print(z)

# #14
# socials = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# j = socials.split(",")
# print(j)

# #15
# string1 = "_Coding For All_"
# print(string1[0])

# #16
# print(string1[-1])

# #17
# print(string1[10])

# #18
# create_acronym = "Python For Everyone"
# acronym = ''.join(word[0].upper() for word in create_acronym.split())
# print(acronym)  

# #19
# create_acrnym = "Coding For All"
# acrnym = ''.join(word[0].upper() for word in create_acrnym.split())
# print(acrnym)

# #20
# index = create_acrnym.index("C")
# print(index)

# #21
# ind = create_acrnym.index("F")
# print(ind)

# #22
# x = create_acrnym.rfind("l")
# print(x)

#23
sentence = "You cannot end a sentence with because because because is a conjunction"
y = sentence.find("because")
print(y)

#24
z = sentence.rindex("because")
print(z)

#25
j = z + len("because")
print(sentence[y:z])

#26
#27
#28
substring = "Coding for all"
print(substring.startswith("Coding"))

#29
print(substring.endswith("coding"))

#30
given_str = "  Coding For All  "
print(given_str)

#31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#32
py_libraries = ["Django", "Flask", "Pyramid", "Falcon"]
x = " # ".join(py_libraries)
print(x)

#33
print("I am enjoying this challenge\nI just wonder what is next")

#34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

#35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

#36
a = 8
b = 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {round(a*b, 2)}")
print(f"{a} / {b} = {a/b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")


