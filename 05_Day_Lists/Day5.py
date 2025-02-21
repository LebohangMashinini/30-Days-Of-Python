#Day 5
#Exercises

#1
lis = []

#2
names = ["Lee", "Reba", "Neo", "Palesa", "Kg", "Lesedi", "Andy"]

#3
print(f"Length of the list of names: {len(names)}")

#4
first_name = names[0]
print(f"first item: {first_name}")
middle_name = names[3]
print(f"middle item {middle_name}")
last_name = names[6]
print(f"last item: {last_name}")

#5
mixed_data_type = ["Lee", 20, 154, "single", "1020 Nyati Str"]

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
print(it_companies)

#8
print(f"Number of companies: {len(it_companies)}")

#9
first_company = it_companies[0]
print(first_company)
second_company = it_companies[3]
print(second_company)
last_company = it_companies[6]
print(last_company)


#10


#11
it_companies.insert(7, "Samsung")
print(it_companies)

#12
it_companies.insert(4, "Dell")
print(it_companies)

#13
it_companies[3] = it_companies[3].upper()
print(it_companies)

#14
join_str = "#; ".join(it_companies)
print(join_str)

#15
if "Samsung" in it_companies:
    print("Company is in the list")
else:
    print("Company not in the list")

#16
it_companies.sort()
print(it_companies)

#17
it_companies.reverse()
print(it_companies)


#18
sliced = it_companies[0:3]
print(sliced)

#19
reversed_sliced = it_companies[-3:]
print(reversed_sliced)

#20
start_len_of_list = len(it_companies) // 2
end_len_of_list = len(it_companies) // 2

mid_sliced = it_companies[start_len_of_list:end_len_of_list+1]
print(mid_sliced)

#21
# del it_companies[0]
# print(it_companies)

# #22
# del it_companies[start_len_of_list:end_len_of_list+1]
# print(it_companies)

#23
del it_companies[-1]
print(it_companies)

#24

