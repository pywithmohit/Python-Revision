# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers():
    a = 5
    b = 7
    return(a + b)
add_two_numbers()

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def Area_0f_circle():
    r = 5.18
    pie = 3.14
    area = pie*r*r
    return(area)
Area_0f_circle()

# Write a function called  which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.

def sum_all(*args):
   for item in args:
      if not isinstance(item,(int,float)) or isinstance(item,(bool)):
         return f"Sum is not allowed: {i} is not a number."
      return sum(args)
print(sum_all(15+15+15-15))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
#  Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def mausam(Cel): 
   Fahrenheit = (Cel * 9/5) + 32
   return Fahrenheit
print(mausam(45))

# Write a function called check-season, 
# it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month <= 3 and month >= 1:
        return("This is the winter season.")
    elif month >= 4 and month <= 6:
        return("Thiis is the summer season.")
    elif month >= 7 and month <= 8:
        return("This is the Spring season")
    elif month >= 9 and month <= 12:
        return("This month is Autumn season")
    else:
        return "Enter a valid month"
print(check_season(44))

# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1,x2,y1,y2):
    if x1 - x2 == 0:
        return " Undifined(Vartical Line) "
    slope = (x2-x1)/(y1-y2)
    return slope
print(calculate_slope(1,2,3,9))


# Declare a function named print_list.
#  It takes a list as a parameter and it prints out each element of the list.

def print_list(lst):
    for item in lst:
        print(item)

my_lst = ["Apple","Banana","Grapes","Redbull"]
print_list(my_lst)


# Declare a function named reverse_list.
#  It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(lst):
  reversed_lst = []
  for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])
  return reversed_lst

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items():
    lst = ["apple","banana","grapes"]
    return [item.capitalize() for item in lst]

print(capitalize_list_items())

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]


def add_item(food_list,new_item):
    food_list.append(new_item)
    return food_list
my_food = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(my_food,'Meat'))

def add_num(int_num,int_value):
    int_num.append(int_value)
    return int_num
numbers = [2, 3, 7, 9]
print(add_num(numbers,15))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(my_lst, item_to_remove):
    new_list = []
    for current_item in my_lst:
        if current_item != item_to_remove:
            new_list.append(current_item)

    return new_list

my_food = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(my_food, 'Mango'))
