""" Problem:
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def first_positive(lst):
    if len(lst) == 0: return 1
    list_ = sorted(set(lst))
    integer = 1
    list_positive = []

    for i, item in enumerate(list_):
        if item > 0:
            list_positive = list_[i::]
            break

    for i in range(len(list_positive)):
        if list_positive[i] != integer:
            return integer
        else:
            integer += 1
    return integer


def main():
    assert first_positive([]) == 1
    assert first_positive([0]) == 1
    assert first_positive([1]) == 2
    assert first_positive([-5]) == 1
    assert first_positive([1, 2, 0]) == 3
    assert first_positive([3, 4, -1, 1]) == 2
    assert first_positive([3, 1, 8, 2, 5, 1, 2]) == 4
    assert first_positive([1, 2, 3, 4, 5, 6, 7, 9]) == 8
    assert first_positive([6, -14, -8, -2, -3, 1, 2]) == 3


if __name__ == '__main__':
    main()