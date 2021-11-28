import datetime as dt


def get_weekend_count(year=None, month=None, day=None):
    """Returns count of weekend days in month
    """
    if year and month and day:
        today = dt.date(year, month, day)
    else:
        today = dt.date.today()
        year = today.year
        month = today.month

    if month in (1, 3, 5, 7, 8, 10, 12):
        days_count = 31
    elif month in (4, 6, 9, 11):
        days_count = 30
    else:
        days_count = 28
        if (year // 4 == 0) and not (year // 100 == 0):
            days_count = 29

    weekend_count = 0
    for day in range(1, days_count):
        weekday = dt.date(year, month, day).weekday()
        if weekday in (5, 6):
            weekend_count += 1

    return weekend_count
