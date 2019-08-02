from datetime import date


def get_date_from_string(date_string):
    date_string = date_string.split('/')

    day = int(date_string[0])
    month = int(date_string[1])
    year = int(date_string[2])

    return date(year, month, day)
