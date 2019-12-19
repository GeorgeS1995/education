def recurse_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return int(arr.pop(0)) + recurse_sum(arr)


input_list = list(input('input_list: '))
print(recurse_sum(input_list))


