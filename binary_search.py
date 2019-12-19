
def smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def sort_smallest(arr):
    newarr = []
    for i in range(len(arr)):
        smallest_value = smallest(arr)
        newarr.append(arr.pop(smallest_value))
    return newarr


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid, guess
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1


input_list = list(input('Inptu sorted list: '))
input_item = input('Input item: ')
sorted_input_list = sort_smallest(input_list)
result_index, result_value = binary_search(sorted_input_list, input_item)

print('Index: {0}\nValue: {1}'.format(result_index, result_value))