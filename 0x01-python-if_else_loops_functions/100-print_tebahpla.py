#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    if char % 2 == 0:
        char2 = 0
    else:
        char2 = 1
    print("{:s}".format(chr(char - (32 * char2))), end="")
