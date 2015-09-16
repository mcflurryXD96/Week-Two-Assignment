#
__author__ = 'Daniel McMurray'

# CIS 125
# Convert Fahrenheit to Celsius
#
# This program prompts the user for a temperature in Fahrenheit, converts it to Celsius, and prints out the results.


F = eval(input("Please enter a temp in Fahrenheit: "))

C = (F-32) * 5 / 9

print("The temp ", F, " in Fahrenheit is equal to ", C, " Celsius")
