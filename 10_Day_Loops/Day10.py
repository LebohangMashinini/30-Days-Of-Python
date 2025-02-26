#Exercises: Day 10
#Exercises: Level 1
#1
for num in range(0, 10+1):
    print(num)

count = 0
while count < 11:
    print(count)
    count += 1

#2
for number in range(10, 0-1, -1):
    print(number)


counter = 10
while counter > 0-1:
    print(counter)
    counter -= 1

#3
height = 8
for i in range(height):
        print("#" * (i + 1))

#4
s_height = 8
for _ in range(s_height):
        print("# " * s_height)

#5
for number in range(0, 10+1):
        print(f"{number} x {number} = {number * number}")

#6
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
        print(item)

#7
for number in range(0, 100+1):
        if number % 2 == 0:
                print(number)

#8
for num in range(0, 100+1):
        if num % 2 != 0:
                print(num)


