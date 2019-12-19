def count_of_elem_recurse(arr):
    if arr == []:
        return 0
    else:
        return 1 + count_of_elem_recurse(arr[1:])


input_list = list(input('input_list: '))
print(count_of_elem_recurse(input_list))
