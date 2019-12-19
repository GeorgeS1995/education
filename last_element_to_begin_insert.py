input_list = list(input('Введите последовательность элементов:'))
print(input_list)
input_list.insert(0, input_list.pop()) #insert() берет на вход номер элемента и каким значение его заменить

print('\nПоследовательность на выходе:\n {}'.format(input_list))