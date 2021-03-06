#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        return x
    except IndexError :
        return sum(map(lambda x:1, my_list))
    finally:
        print(end="\n")
