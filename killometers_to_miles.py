def kilometers_to_miles(x):
    x = 1.6 * x
    return x

NumberOfKM = int(input('input a number of killometers:'))
Func_Res = kilometers_to_miles(NumberOfKM)
print('{0} km is {1} miles'.format(NumberOfKM, Func_Res))
