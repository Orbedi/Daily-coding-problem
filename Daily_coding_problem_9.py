""" Problem:
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should
return 10, since we pick 5 and 5.

"""


def maxSum(list_):
    incl = list_[1]
    excl = list_[0]
    for item in list_[2::]:
        aux_excl = incl if incl > excl else excl
        incl =  excl + item if (excl + item) > item else item
        excl = aux_excl
    return incl if incl > excl else excl


if __name__ == '__main__':
    assert maxSum([5,1,1,5]) == 10
    assert maxSum([1,0,0,0,0]) == 1
    assert maxSum([0,0,0,0,1]) == 1
    assert maxSum([0,0,1,0,1]) == 2
    assert maxSum([1,2,3,4,5]) == 9
    assert maxSum([2,4,6,2,5]) == 13
    assert maxSum([4,1,1,4,2,1]) == 9
    assert maxSum([-1,2,-3,1,5]) == 7
    assert maxSum([4,1,1,-4,2,1]) == 7
    assert maxSum([0,-2,-3,1,-5]) == 1
    assert maxSum([-1,-2,-3,1,-5]) == 1


