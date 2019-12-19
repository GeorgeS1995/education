# Задача о покрытии множества


def add_multiple(dict = {}):
    i = 1
    while True:
        answer = input('Добавить множество?(y/n) ')
        if answer == 'y':
            input_multiple = input('Введите название множества {} '.format(i))
            # set - множество, множество это список без повторяющихся элементов
            input_set = set(list(input('Введите элементы множества через запятую ').split(",")))
            dict[input_multiple] = input_set
            print('Множество добавленно\n{} '.format(dict[input_multiple]))
            i += 1
        else:
            break
    print('Множества добавлены: \n{}'.format(dict))
    return dict


def best_cover_def(multiplies):
    def all_item(multiplies):
        # Фиксирую все элементы множеств
        all_items = []
        for multiple, item in multiplies.items():
            for i in item:
                all_items.append(i)
        all_items = set(all_items)
        return all_items
    covered = set()
    all = all_item(multiplies)
    outputdicthead = []
    while all != covered:
        # Создал временный словарь с не входящими в покрытие элементами
        tempdict = {}
        for multiple, item in multiplies.items():
            item_not_in_cover = item - covered
            tempdict[multiple] = item_not_in_cover
        templen = 0
        # определяю наибольшее множество из temdict
        for multiple, item in tempdict.items():
            if len(item) > templen:
                chosen = item
                outputdicthead.append(multiple)
                templen = len(item)
        covered = covered | chosen
    return outputdicthead

multiplies = add_multiple()

print(best_cover_def(multiplies))

