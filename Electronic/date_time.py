from datetime import datetime

DATE_MASK = '%d.%m.%Y %H:%M'
OUTPUT_MASK = '%e %B %Y year %-H hour{} %-M minute{}'


def date_time(time: str) -> str:

    date = datetime.strptime(time, DATE_MASK)
    return date.strftime(OUTPUT_MASK).format("" if date.hour == 1 else "s", "" if date.minute == 1 else "s").strip()

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
