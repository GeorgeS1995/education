def time_converter(time):
    hours = int(time[0:2])
    minutes = time[3:5]
    if hours > 12:
        time = '{0}:{1} p.m.'.format(hours - 12, minutes)
    elif hours == 12:
        time = '{0}:{1} p.m.'.format(hours, minutes)
    elif hours == 0:
        time = '12:{0} a.m.'.format(minutes)
    else:
        time = '{0}:{1} a.m.'.format(hours, minutes)
    return time

if __name__ == '__main__':
    print("Example:")
    print(time_converter('00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")