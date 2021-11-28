import datetime as dt


def get_weekend_count():
    today = dt.date.today()
    year = today.year
    month = today.month
    feb_count = 28
    weekend_count = 0
    if (year // 4 == 0) and not (year // 100 == 0):
        feb_count = 29
    days_count = feb_count
    if month in (1, 3, 5, 7, 8, 10, 12):
        days_count = 31
    if month in (4, 6, 9, 11):
        days_count = 30
    for day in range(1, days_count):
        weekday = dt.date(year, month, day).weekday()
        if weekday in (5, 6):
            weekend_count += 1
    return weekend_count
