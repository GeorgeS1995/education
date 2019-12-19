#по рекомендации Вано рассчет количества элементов идет внутри функции, на вход одно значение
def last_elem_to_begin (elem):
    i = len(elem) - 1 #Так как отсчет с 0 идет
    last_elem = elem[len(elem) - 1] #Запоминаю последний элемент, так как конструкция ниже делает из 12345 11234
    while i > 0:
        elem[i] = elem[i - 1]
        i -= 1
    elem[0] = last_elem
    return elem

def input_list():
    input_list = [] # Создал пустой список которй буду наполнять
    while True:
        input_elem = input('Введите элемент:')
        input_list.append(input_elem)
        con = input('добавить еще элемент y/n:')
        if con == 'n' or con == 'no':
            break
    return input_list

print('Последоваотельность на выходе:\n {}'.format(last_elem_to_begin(input_list())))

