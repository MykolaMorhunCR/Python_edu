import datetime


def check_my_date(day, month, year):
    isValidDate = True
    # BC_Flag = False
    # if year < 0:
    #     year = abs(year)
    #     BC_Flag = True
    try:
        datetime.datetime(int(year), int(month), int(day))

    except ValueError:
        isValidDate = False

    if isValidDate:
        return True
    else:
        return False


# if check_my_date(10, 12, 1):
#     print('1')
# else:
#     print('0')
#

