#!/usr/bin/python3
import random
number = -626
if number < 0:
    last_digit = ((number * -1) % 10) * -1
else:
    last_digit = number % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and not 0:
    e = " and is less than 6 and not 0"
    print(f"Last digit of {number} is {last_digit}" + e)

