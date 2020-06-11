import numpy as np


class Arrays:

    def __init__(self, input_array):
        self.main_array = input_array

    def find_mean(self):
        mean = np.mean(self.main_array)
        print(mean)
        return mean

    def Bounds(self, n=0):
        new_array = [None] * len(self.main_array)
        upper_bound = Arrays.find_mean(self) + (Arrays.find_mean(self) * 0.2)
        lower_bound = Arrays.find_mean(self) - (Arrays.find_mean(self) * 0.2)

        for i in range(0, len(self.main_array)):
            if upper_bound > self.main_array[i] > lower_bound:
                new_array[n] = self.main_array[i]
                n += 1

        close_to_mean = list(filter(None, new_array))
        print(close_to_mean)
        return close_to_mean

    def maximum(self):
        sorted_array = np.unique(np.sort(self.main_array))
        reverse_sorted_array = sorted_array[::-1]
        max1 = reverse_sorted_array[0]
        if len(reverse_sorted_array) > 1:
            max2 = reverse_sorted_array[1]
        else:
            max2 = None
        return max1, max2


# Array = Arrays(np.random.randint(-1000, high = 1000, size = 1000))
# Array.find_mean()
# Array.Bounds()