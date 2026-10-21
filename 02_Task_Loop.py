# Iterate 0 to 10 using for loop, do the same using while loop.
num = 0
while num <= 10:
    print(num)
    num += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
num = 10
while num >= 0:
    print(num)
    num -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#
##
###
####
#####
######
#######

for i in range(0,8):
    print("#"*i)

# Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(0,11):
    print(f"{i} x {i} = {i*i}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.

items = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in items:
    print(i)

# Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(101):
    if i % 2 == 0 :
     print(i)

 # Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(101):
    if i % 2 != 0 :
     print(i)


# Use for loop to iterate from 0 to 100 and print the sum of all numbers.

total = 0
for i in range(101):
    total += i
print(total)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

odd_total = 0
even_total = 0
for i in range(101):
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i

print("Even total : ",even_total)
print("Odd total : ",odd_total)

# Loop through the countries and print those containing "land".
from countries import countries
for country in countries:
    if "land" in country.lower():
        print(country)

#  This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
reverse_list = []
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruits)-1,-1,-1):
    reverse_list.append(fruits[i])
print(reverse_list)

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world

import json
from collections import Counter
from pathlib import Path

data_file = Path(__file__).with_name("countries_data.py")
with data_file.open(encoding="utf-8") as file:
    countries_data = json.load(file)

language_counts = Counter(
    language
    for country in countries_data
    for language in country["languages"]
)
print("Total number of languages:", len(language_counts))

print("Ten most spoken languages (by number of countries):")
for language, country_count in language_counts.most_common(10):
    print(f"{language}: {country_count}")

print("Ten most populated countries:")
most_populated = sorted(
    countries_data,
    key=lambda country: country["population"],
    reverse=True,
)[:10]
for country in most_populated:
    print(f"{country['name']}: {country['population']}")


