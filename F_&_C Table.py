#
__author__ = 'Daniel McMurray'

# CIS 125
# Print Fahrenheit and Celsius Table
#
# This program computes and prints a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees from 0C to 100C.


def main():
    for C in range(0,101,10):
        F = (9/5 * C) + 32
        print(C,F)
main()
