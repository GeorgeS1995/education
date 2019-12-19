def last_elem_to_begin(count_elem, elem):
    i = count_elem - 1 #Так как отсчет с 0 идет
    last_elem = elem[count_elem - 1] #Запоминаю последний элемент так как конструкция ниже делает из 12345 11234
    while i > 0:
        elem[i] = elem[i - 1]
        i -= 1
    elem[0] = last_elem
    return elem

input_list = list(input('Ввудите любую последовательность элементов:'))

print('Количество элементов: {}'.format(len(input_list)))
print(last_elem_to_begin(len(input_list), input_list))



