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


def product_of_each_element_left_right(list_):
    temp = 1
    result = [1] * len(list_)
    for i,elem in enumerate(list_):
        result[i] = temp
        temp *= elem
    temp = 1
    for i in range(len(list_)-1, -1, -1):
        result[i] *= temp
        temp *= list_[i]
    return result


def main():
    list_ = [2.5, 7.6, 1.2]
    list_ = [3, 5, 2, 1, 6]
    print(product_of_each_element(list_))
    print(product_of_each_element_with_division(list_))
    print(product_of_each_element_left_right(list_))


if __name__ == '__main__':
    main()