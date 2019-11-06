#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
length_given = float(input("Please enter the length:\t"))
width_length = float(input("Please enter the width:\t"))

# calculate area
area = length_given * width_length
area = round(area, 2)
            
# calculate perimeter
perimeter = length_given * 2 + width_length * 2

# format and display the result
print()
print("Area:\t" + str(area))
print("Perimeter:\t" + str(perimeter))
print()
print("Thanks for using this program!")
print()
print("Bye")
