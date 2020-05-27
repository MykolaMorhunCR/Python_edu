import numpy as np

input_array = np.random.randint(-1000, high=1000, size=1000)


def find_mean(main_array):
    mean = np.mean(main_array)

    return mean


def Bounds(main_array, n=0):
    new_array = [None] * len(main_array)
    upper_bound = find_mean(main_array) + (find_mean(main_array) * 0.2)
    lower_bound = find_mean(main_array) - (find_mean(main_array) * 0.2)

    for i in range(0, len(main_array)):
        if upper_bound > main_array[i] > lower_bound:
            new_array[n] = main_array[i]
            n += 1

    close_to_mean = list(filter(None, new_array))

    return close_to_mean


def maximum(main_array):
    sorted_array = np.unique(np.sort(main_array))
    reverse_sorted_array = sorted_array[::-1]
    maximum_values = [reverse_sorted_array[0], reverse_sorted_array[1]]
    return maximum_values


find_mean(input_array)
maximum(input_array)
