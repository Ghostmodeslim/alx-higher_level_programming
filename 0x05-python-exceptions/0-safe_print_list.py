#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    the_list = 0
    for a in range(x):
        try:
            print('{}'.format(my_list[a]), end="")
            the_list += 1
        except IndexError:
            pass
    print("")
    return (the_list)
