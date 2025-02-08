#Exercise

#1
age = int(20)

#2
height = float(1.65)

#3
comp_num = complex(5+2j)

#4
base = int(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

#5
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

#6
length = float(input("Enter lenght: "))
width = float(input("Enter width: "))
area = length * width
print(f"The area of a rectangle is {area}")
perimeter = 2 * (length + width)
print(f"The perimeter of a rectangle is {perimeter}")

#7
radius = float(input("Enter radius: "))
pi = 3.142
area = pi * radius * radius
print(f"The are of a circle is {area}")
circumference = 2 * pi * radius
print(f"The circumference of a circle is {circumference}")

#8
#x intercept
#equation: 2x - 2
y_to_zero = 0
x_to_zero = 0
x_intercept = 1
y_intercept = -2

slope = (y_intercept - y_to_zero) / (x_to_zero - x_intercept)
print(slope)

#9
x1 = 2
x2 = 2
y1 = 6
y2 = 10
m = (y2 - y1) / (x2 - x1)
print(m)

#10
print(slope == m)
print(slope > m)
print(slope < m)
print(slope != m)
print(slope >= m)
print(slope <= m)

#11
y = 0
x = -3
value_y = -3 ** 2 + 6 * -3 + 9
print(value_y)

#12
len_python = len("python")
len_dragon = len("dragon")
print(len_python != len_dragon)

#13
if "on" in "python" and "dragon":
    print(True)

#14
sentence = "I hope this course is not full of jargon"
for word in sentence:
    if "jargon" in sentence:
        print(True)

#15