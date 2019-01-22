def sun_angle(time):

    hours = int(time[0:2])
    minutes = int(time[3:5]) / 60

    if 6 <= hours + minutes <= 18:
        return (hours - 6 + minutes) / 12 * 180
    else:
        return "I don't see the sun"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
