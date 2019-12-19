import sys, warnings


if sys.version_info[0] < 3:
    warnings.warn('Для выполнения этой программы необходима как минимум веросия Python 3.0',
                  RuntimeWarning)
else:
    print('все окей')