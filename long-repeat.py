def long_repeat(line):
    output = dict()
    output_list = []
    for i, v in enumerate(line):
        if output.get(v) == None:
            output[v] = 1
        elif output.get(v) > 1 and output.get(line[i - 1]) != output.get(v):
            output[v] =1
        else:
            output[v] = output[v] + 1
    if output == {}:
        return 0
    else:
        for i in output.values():
            output_list.append(i)
        return max(output_list)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')