#!/usr/bin/env python3
def only_positive(input_list):
    count = 0
    while len(input_list) > count:
        a = int(input_list[count])
        if a < 0:
            input_list.remove(input_list[count])
        else:
            count += 1
    return input_list

input_int = input('list: ')
input_int = list(input_int.split(' '))
print(only_positive(input_int))
