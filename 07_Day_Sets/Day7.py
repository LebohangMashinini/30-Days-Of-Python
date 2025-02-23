#Exercises: Day 7
#Exercises: Level 1
# sets
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


# #1
# print(len(it_companies))

# #2
# it_companies.add("Twitter")
# print(it_companies)

# #3
# more_it_companies = {'Samsung', 'Dell', 'Intel','HP'}
# it_companies.update(more_it_companies)
# print(it_companies)

# #4
# it_companies.remove("Facebook")
# print(it_companies)

# #5
# difference = "The remove method will raise an error if the specified item does not exist and Discard method does not raise an error."
# print(f"What is the difference between remove and discard? {difference}")


#Exercises: Level 2
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}

#1
print(a.union(b))


#2
print(a.intersection(b))

#3
print(a.issubset(b))

#4
print(a.isdisjoint(b))

#5
a.update(b)
b.update(a)

#6
a.symmetric_difference(b)
print(a)

#7
del a
del b

#Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1
