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
        # Создаем базовый массив для заполнения в будущем. Массив создан для двузначного билета, где Количество вариантов сумм всегда равно одному.
        # В дальнейшем каждый элемент списка - это количество вариантов составления суммы цифр Далее N(k). Порядок - по возрастанию суммы.
        array = [1] * 10 + [0] * (num // 2 * 9 - 9)
        # Количество итераций цикла зависит от количества номеров в билете. Для каждого последующего увеличения номера необходима еще одна итерация. Т.к. номера четные то прибавляется две цифры
        # К его номеру. Отсюда деление на два для каждого последующего увеличения
        for i in range(num // 2 - 1):
            #На каждой итерации массив обновляется данными для последующего количества номеров в билете (1 итер - двузначый, 2 итер - четырехзначный и т.д.)
            #Каждый элемент вычисляется путем суммирования всех N(k) до данной позиции включительно используя массив созданный на предыдущей итерации
            array = [sum(array[:x + 1]) if x < 10 else sum(array[x - 9:x + 1]) for x in range(len(array))]
        sum_of_lucky = sum([x ** 2 for x in array])
        print(sum_of_lucky)
        return sum_of_lucky



#try:
    #lucky(-10)
#except ValueError:
    #print("Ticket number can't be 0 and less")
#else:
    #pass
