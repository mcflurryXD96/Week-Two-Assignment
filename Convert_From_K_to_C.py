#
__author__ = 'Daniel McMurray'

# CIS 125
# Convert Kelvin to Celsius
#
# This program prompts the user for a distance measured in kilometers, converts it to miles, and prints out the results. One kilometer is approximately 0.62 miles.


K = eval(input("Please enter a distance in kilometers: "))

M = K * .62137119224

print("The distance ", K, " in kilometers is equal to ", M, " Miles")
