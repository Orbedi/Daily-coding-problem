""" Problem:
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function
that returns the number of unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
•	1, 1, 1, 1
•	2, 1, 1
•	1, 2, 1
•	1, 1, 2
•	2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

"""


# Brute force for 1 or 2 steps:
def staircase(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return staircase(n - 1) + staircase(n - 2)


# Memoization for 1 or 2 steps:
def memo_staircase(n):
    result = [0] * (n+1)
    result[n] = 1
    result[n-1] = 1
    for i in range(n-2, -1, -1):
        result[i] = result[i+1] + result[i+2]
    return result[0]


# Memoization for x steps:
def memo_staircase_x(n, x):
    result = [0] * (n+1)
    result[n] = 1
    for i in range(n, -1, -1):
        for s in x:
            if i + s <= n:
                result[i] += result[i+s]
    return result[0]


if __name__ == '__main__':    
    assert staircase(0) == 1
    assert staircase(1) == 1
    assert staircase(2) == 2
    assert staircase(4) == 5
    assert staircase(5) == 8

    assert memo_staircase(0) == 1
    assert memo_staircase(1) == 1
    assert memo_staircase(2) == 2
    assert memo_staircase(4) == 5
    assert memo_staircase(5) == 8

    assert memo_staircase_x(0, [1, 2]) == 1
    assert memo_staircase_x(1, [1, 2]) == 1
    assert memo_staircase_x(2, [1, 2]) == 2
    assert memo_staircase_x(4, [1, 2]) == 5
    assert memo_staircase_x(5, [1, 2]) == 8

    assert memo_staircase_x(2, [1]) == 1
    assert memo_staircase_x(2, [2]) == 1
    assert memo_staircase_x(6, [2]) == 1
    assert memo_staircase_x(5, [3, 5]) == 1
    assert memo_staircase_x(8, [3, 5]) == 2
    assert memo_staircase_x(4, [1, 3, 5]) == 3
    assert memo_staircase_x(5, [1, 3, 5]) == 5
    assert memo_staircase_x(8, [1, 2, 5]) == 44
