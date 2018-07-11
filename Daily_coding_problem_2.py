
""" Problem:
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_of_each_element(list_):
    result = [1] * len(list_)
    for i, elem_i in enumerate(list_):
        for j, elem_j in enumerate(list_):
            if i != j:
                result[i] *= elem_j
    return result


# If there is a zero in the list, this method will not work correctly
def product_of_each_element_with_division(list_):
    result = [1] * len(list_)
    for i, elem in enumerate(list_[1::]): result[0] *= elem
    for i in range(1, len(list_)):
         result[i] = int((result[i-1] / list_[i]) * list_[i-1])
    return result


def product_of_each_element_left_to_right(list_):
    aux = 1
    result = [1] * len(list_)
    for i,elem in enumerate(list_):
        result[i] = aux
        aux *= elem
    aux = 1
    for i in range(len(list_)-1, -1, -1):
        result[i] *= aux
        aux *= list_[i]
    return result


def main():
    list_ = [2.5, 7.6, 1.2]
    list_ = [3, 5, 2, 1, 6]
    print(product_of_each_element(list_))
    print(product_of_each_element_with_division(list_))
    print(product_of_each_element_left_to_right(list_))


if __name__ == '__main__':
    main()