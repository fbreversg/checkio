from datetime import datetime
from calendar import day_name


def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """

    firstweek = set(range(datetime(year, 1, 1).weekday(), 7))   # weekday 0..6
    lastweek = set(range(datetime(year, 12, 31).isoweekday()))  # isoweekday 1..7
    return [day_name[day] for day in sorted((firstweek & lastweek) or (firstweek | lastweek))]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
