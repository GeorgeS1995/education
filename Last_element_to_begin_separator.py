def last_elem_to_begin(elem):
    i = len(elem) - 1 #Так как отсчет с 0 идет
    last_elem = elem[i] #Запоминаю последний элемент так как конструкция ниже делает из 12345 11234
    while i > 0:
        elem[i] = elem[i - 1]
        i -= 1
    elem[0] = last_elem
    return elem

input_list = input('Ввудите любую последовательность элементов(разделяя |):')
print('Количество элементов: {}'.format(len(input_list)))
print('Результат\n{}'.format(last_elem_to_begin(input_list.split('|'))))



