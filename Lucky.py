import sys


def lucky(num):
    if type(num) is not int:
        raise TypeError("Only integers allowed")
    elif num % 2 != 0:
        raise ValueError("Lucky ticket number should be even")
    elif num <= 0:
        raise ValueError("Ticket number can't be 0 and less")
    elif num >= sys.maxsize:
        raise ValueError("Max value reached")

    else:
        # Because magic
        array = [1] * 10 + [0] * (num // 2 * 9 - 9)

        for i in range(num // 2 - 1):
            array = [sum(array[:x + 1]) if x < 10 else sum(array[x - 9:x + 1]) for x in range(len(array))]
        sum_of_lucky = sum([x ** 2 for x in array])
        print(sum_of_lucky)
        return sum_of_lucky


#lucky(6)
#try:
    #lucky(-10)
#except ValueError:
    #print("Ticket number can't be 0 and less")
#else:
    #pass
