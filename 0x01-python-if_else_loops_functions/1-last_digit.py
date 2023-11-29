#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#next line conver the number to a string
conv_string = str(number)
#next line use string manipulation to get last digit
l_digit = conv_string[-1]
#it is good practice to first treat negative numbers
if number < 0:
    l_digit = "-" + l_digit
#let's first print the random number and the extracted last digit
print(f"Last digit of {number} is {l_digit} and", end=" ")

#Next lines would say the more about the extracted last digit
if int(l_digit) > 5:
    print(f"is greater than 5")
elif int (l_digit) == 0:
    print(f"is 0")
else:
    print(f"is less than 6 and not 0")
