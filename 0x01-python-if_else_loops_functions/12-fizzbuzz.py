#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print_value = "FizzBuzz"
        elif i % 3 == 0:
            print_value = "Fizz"
        elif i % 5 == 0:
            print_value = "Buzz"
        else:
            print_value = i
        print("{}".format(print_value), end=" ")
