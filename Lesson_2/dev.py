# import all the required libraries

import math
# calculate the area of a circle
def circle(r):
    return math.pi * r **2 

# calculate the area of a rectangle

def rectangle(l,w):
    return l * w

# calculate the area of a triangle

def triangle(b,h):
    return b * h * 0.5

# define the main function
def shape_calculator():
    raduies = float(input("please enter the raduies : "))
    print(f"your result is :  {circle(raduies)}")
    length = float(input("please enter the length of rectangle : "))
    wedth = float(input(" please enter the wedth of rectangle : "))
    print(f"the result of the area is : {rectangle(length,wedth)}")



# call the function 
shape_calculator()