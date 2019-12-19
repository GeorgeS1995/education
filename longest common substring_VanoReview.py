def longest_common_substring(word_a, word_b):
    # словарь где хранятся значения в клеточках "таблицы"
    cell_dict = {}
    # Маленький движ что б не улететь за таблицу находясь в координате 1:1
    cell_dict[0] = {}
    cell_dict[0][0] = 0
    # сам алгоритм поиска самой длинной общей подстроки, начинаю с координаты 1:1
    for index_a, value_a in enumerate(word_a, start=1):
        # Вероятно это можно, но как сразу создать "вложенны" словарь я не допер
        cell_dict[index_a] = {}
        for index_b, value_b in enumerate(word_b, start=1):
            # огораживаем таблицу нулями что б не вылететь в "пустую" клетку
            cell_dict[index_a][0] = 0
            cell_dict[0][index_b] = 0
            if value_a == value_b:
                cell_dict[index_a][index_b] = cell_dict[index_a - 1][index_b - 1] + 1
            else:
                cell_dict[index_a][index_b] = 0
    print(cell_dict)
    # Ищу максимальное значение в вложенном словаре, для этого пробегаю по всему словарю, иначе выдает максимальную координату
    maximum = 0
    for i_big in cell_dict.values():
        for i_big_indexies, i_big_values in i_big.items():
            if i_big_values > maximum:
                maximum = i_big_values
                # фиксирую координату (то есть порядковый номер)последней буквы и вычитая размер строки "вырезаю" само строку
                longest_string = word_b[i_big_indexies - i_big_values : i_big_indexies]
                print(longest_string)
    return maximum, longest_string

print(longest_common_substring(input('Введите слово 1: '), input('Введите слово 2: ')))