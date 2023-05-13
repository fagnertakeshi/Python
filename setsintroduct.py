from functools import reduce


def average(array):
    sum_array=reduce(lambda x, y: x+y, set(array))
    return float(sum_array/len(set(array)))
