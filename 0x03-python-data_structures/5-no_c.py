#!/usr/bin/python3
def no_c(my_string):
    main_str = ""
    for num in my_string:
        if num != 'c' and num != 'C':
            main_str += num
    return main_str
