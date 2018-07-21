def decoded(message, memo=True):
    len_ = len(message)
    if memo:
        array = [None] * (len_ + 1)
        return decoded_memo(message, array, len_)
    return decoded_recursive(message, len_)


# Recurrence:
def decoded_recursive(message, i):
    if i == 0:
        return 1
    current = len(message) - i
    if message[current] == '0':
        return 0
    result = decoded_recursive(message, i - 1)
    if i >= 2 and int(message[current:current+2]) <= 26:
        result += decoded_recursive(message, i - 2)
    return result


# Memoization and recurrence:
def decoded_memo(message, array, i):
    if i == 0:
        return 1
    current = len(message) - i
    if message[current] == '0':
        return 0
    if array[current] is not None:
        return array[current]
    result = decoded_memo(message, array, i - 1)
    if i >= 2 and int(message[current:current + 2]) <= 26:
        result += decoded_memo(message, array, i - 2)
    array[current] = result
    return result


def main():

    # Only recurrence:
    assert decoded('', False) == 1
    assert decoded('0', False) == 0
    assert decoded('1', False) == 1
    assert decoded('12', False) == 2
    assert decoded('26', False) == 2
    assert decoded('111', False) == 3
    assert decoded('123', False) == 3
    assert decoded('10100', False) == 0
    assert decoded('11111', False) == 8
    assert decoded('12121', False) == 8

    # Using memoization and recurrence:
    assert decoded('') == 1
    assert decoded('0') == 0
    assert decoded('1') == 1
    assert decoded('12') == 2
    assert decoded('26') == 2
    assert decoded('111') == 3
    assert decoded('123') == 3
    assert decoded('10100') == 0
    assert decoded('11111') == 8
    assert decoded('12121') == 8


if __name__ == '__main__':
    main()