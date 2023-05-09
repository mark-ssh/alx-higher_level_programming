#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number >= 0:
    _lastdigit = number % 10
elif number < 0:
    _lastdigit = ((number * -1) % 10) * -1
if _lastdigit > 5:
    str = 'Last digit of {0} is {1} and is greater than 5'
elif _lastdigit < 6 and _lastdigit != 0:
    str = 'Last digit of {0} is {1} and is less than 6 and not 0'
elif _lastdigit == 0:
    str = 'Last digit of {0} is {1} and is 0'

print(str.format(number, _lastdigit))
