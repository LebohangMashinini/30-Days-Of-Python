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
it_companies.clear()
print(it_companies)

#25
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

join_list = front_end + back_end
print(join_list)

#27
full_stack = join_list
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

#Exercises: Level 2

#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minimum = min(ages)
maximum = max(ages)
print(ages)
print(minimum)
print(maximum)

ages.insert(10, minimum)
print(ages)

ages.insert(11, maximum)
print(ages)

print(f"og list: {str(ages)}")
ages.sort()
mid = len(ages) // 2
median = (ages[mid] + ages[~mid]) / 2

print(f"median list {str(median)}")

sum = sum(ages)
average = sum // len(ages)
print(average)

range = maximum - minimum
print(range)

compare_min = (minimum - average)
print(abs(compare_min))
compare_max = (maximum -  average)
print(abs(compare_max))

#1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
mid = len(countries) // 2
start = countries[:mid]
end = countries[mid:]
print(f"list 1 {start}")
print(f"list 2 {end}")

#3
lst = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *rest = lst
print(first)
print(second)
print(third)
print(rest)