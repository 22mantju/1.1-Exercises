#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 2)

# calculate total gas cost
tgs = gallons_used * cost_per_gallon
tgs = round(tgs, 2)

# calculate cost per mile
cpm = cost_per_gallon * gallons_used / miles_driven

# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost:\t\t" + str(tgs))
print("Cost per mile:\t\t" + str(cpm))
print()
print("Bye")
