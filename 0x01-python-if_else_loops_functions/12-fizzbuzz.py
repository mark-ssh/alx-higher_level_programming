#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            num = "FizzBuzz"
            print("{:s} ".format(num), end="")
        elif num % 5 == 0:
            num = "Buzz"
            print("{:s} ".format(num), end="")
        elif num % 3 == 0:
            num = "Fizz"
            print("{:s} ".format(num), end="")
        else:
            print("{:d} ".format(num), end="")
