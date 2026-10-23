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


