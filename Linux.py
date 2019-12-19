#!/usr/bin/env python3
def last_elem_to_begin(elem):
    i = len(elem) - 1
    last_elem = elem[len(elem) - 1]
    while i > 0:
        elem[i] = elem[i - 1]
        i -= 1
    elem[0] = last_elem
    return elem


input_list = list(input('Input elements:'))

print('Count of elements: {}'.format(len(input_list)))
print('\nOutput {}'.format(last_elem_to_begin(input_list)))