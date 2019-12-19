def sun_angle(time):
    time = int(time[0:2]) + int(time[3:5]) / 60
    if time < 6 or time > 18:
        time = "I don't see the sun!"
    else:
        time = (180 / 12) * (time - 6)
    return time

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")