def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        opor = int(arr[0])
        less = [i for i in arr[1:] if int(i) <= opor]
        greater = [i for i in arr[1:] if int(i) > opor]
        return quicksort(less) + [opor] + quicksort(greater)


input_list = list(input('input_list: '))
print(quicksort(input_list))