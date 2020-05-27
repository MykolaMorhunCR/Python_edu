import datetime


def date(day, month, year):
    isValidDate = True

    try:
        datetime.datetime(int(year), int(month), int(day))

    except ValueError:
        isValidDate = False

    if isValidDate:
        print ("Yes")
    else:
        print ("No")


date(10, 12, "two")
date(31, 11, 2000)
