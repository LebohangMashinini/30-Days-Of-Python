# Exercises: Day 8
#1
dog = {}

#2
dog['name'] = 'Rocky'
dog['color'] = 'White'
dog['breed'] = 'Husky'
dog['legs'] = 4
dog['age'] = 3
print(dog)

#3
student = {
    "first_name": "Lee",
    "last_name": "Mashinini",
    "gender": "Female",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "DBMongo", "Firebase", "HTML", "CSS"],
    "country": "South Africa",
    "city": "Johannesburg",
    "address": "1020 Nyati Str"
}

#4
print(len(student))

#5
print(type(student['skills']))

#6
student['skills'].append("Flask")
print(student)

#7
keys = student.keys()
print(keys)

#8
values = student.values()
print(values)

#9
print(student.items())

#10
del student['last_name']

#11
del dog
