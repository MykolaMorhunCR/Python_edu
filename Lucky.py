def lucky(num):
    if type(num) is not int:
        raise ValueError("Only integers allowed")
    elif num % 2 != 0:
        raise ValueError("Ticket number can't be odd")
    elif num == 0:
        raise ValueError("Ticket number can't be 0")
    elif num < 0:
        raise ValueError("Ticket number can't be negative")
    else:
        # Because magic

        array = [1] * 10 + [0] * (num / 2 * 9 - 9)

        for i in range(num / 2 - 1):
            array = [sum(array[:x + 1]) if x < 10 else sum(array[x - 9:x + 1]) for x in range(len(array))]
        sum_of_lucky = sum([x ** 2 for x in array])

        return sum_of_lucky
