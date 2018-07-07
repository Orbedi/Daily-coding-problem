import unittest

""" Problem:
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def add_two_num(list_, k):
    for i in range(0, len(list_)):
        for j in range(i+1, len(list_)):
            if list_[i] + list_[j] == k:
                return [list_[i], list_[j]]
    return []


class MyTest(unittest.TestCase):

    def test_one_number(self):
        self.assertEqual(add_two_num([1], 1), [])
        self.assertEqual(add_two_num([1], 2), [])

    def test_two_numbers(self):
        self.assertEqual(add_two_num([1, 0], 1), [1, 0])
        self.assertEqual(add_two_num([1, 0], 3), [])

    def test_several_numbers(self):
        self.assertEqual(add_two_num([1, 0, 2, 4, 6], 10), [4, 6])
        self.assertEqual(add_two_num([1, 2, 4, 7], 10), [])

    def test_empty(self):
        self.assertEqual(add_two_num([], 0), [])
        self.assertEqual(add_two_num([], 7), [])

    def test_decimal_numbers(self):
        self.assertEqual(add_two_num([1.5,3.6,2.5], 4), [1.5, 2.5])
        self.assertEqual(add_two_num([1.5,3.6,2.5], 5.1), [1.5, 3.6])
        self.assertEqual(add_two_num([1.5,3.6,2.5], 4.5), [])


if __name__ == '__main__':
    unittest.main()
