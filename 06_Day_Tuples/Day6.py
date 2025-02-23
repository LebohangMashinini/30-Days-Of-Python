#Exercises: Level 1
#1
tupl = tuple()

#2
brothers = ("Welile", "Sonwabo", "Nceba", "Ntuthuko")
sisters = ("Mpumi", "Bontle", "Ntokozo")

#3
siblings = brothers + sisters
print(siblings)

#4
num_of_siblings = len(siblings)
print(num_of_siblings)

#5
convert = list(siblings)
print(convert)
convert.insert(8,"Portia")
convert.insert(9,"Floyd")
print(convert)

family_members = convert
print(family_members)

#Exercises: Level 2
#1
siblings = family_members[0:7]
parents = family_members[7:]
print(siblings)
print(parents)

#2
fruits = ("apple", "banana", "orange", "grape", "mango")
vegetables = ("carrot", "broccoli", "spinach", "potato", "tomato", "cucumber", "onion", "pepper")
animal_products = ("milk", "honey", "eggs", "wool", "leather", "silk", "cheese", "butter")

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4
middle = len(food_stuff_lt) // 2
start = food_stuff_lt[:middle]
end = food_stuff_lt[middle + 1:]
print(f"list 1 {start}")
print(f"list 2 {end}")

#5
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-3:]
print(f"removed first three: {first_three}")
print(f"removed last three: {last_three}")

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia"  in nordic_countries)
print("Iceland" in nordic_countries)
