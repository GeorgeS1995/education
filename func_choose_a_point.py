import msvcrt


def choose_a_point(elem, exclude):
    number = 1
    output_dict = {}
    for i in elem:
        if i != exclude:
            print('{0} point is {1}'.format(number, i))
            output_dict[number] = i
            number += 1
    while True:
        key = msvcrt.getch()
        try:
            if int(key) in output_dict:
                return print(output_dict[int(key)])
        except ValueError:
            pass


BaudRate = [4800, 7200, 9600, 14400, 119200, 38400, 57600, 115200, 128000]
input_value = int(input("BaudRate exclude: "))
choose_a_point(BaudRate, input_value)


