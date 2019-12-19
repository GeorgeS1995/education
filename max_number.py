def max_number(arr):
    if len(arr) == 2:
        if int(arr[0]) > int(arr[1]):
            return arr[0]
        else:
            return arr[1]
    elif int(arr[0]) > int(arr[1]):
        temp = [arr[0]]
        temp.extend(arr[2:])
        return max_number(temp)
    else:
        return max_number(arr[1:])


input_list = list(input('input_list: '))
print(max_number(input_list))
