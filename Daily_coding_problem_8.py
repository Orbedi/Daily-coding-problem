""" Problem:
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

"""


def unival(tree):
    return count_unival(tree)[0]


def count_unival(node):
    if node is None:
        return 0, True
    result_l = count_unival(node.left)
    result_r = count_unival(node.right)
    result = result_l[0] + result_r[0]
    if result_l[1] and result_r[1]:
        if (node.left is not None and node.val != node.left.val) \
                or (node.right is not None and node.val != node.right.val):
            return result, False
        return result + 1, True
    return result, False


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    nodo1 = Node(1, Node(1, Node(1, Node(1), Node(1))),Node(0, Node(0), Node(0, None, Node(1))))
    nodo2 = Node(1, Node(0), Node(1))
    nodo3 = Node(1)
    nodo4 = Node(1, Node(1, Node(1, Node(0), Node(1)), Node(1)), Node(0, Node(1)))
    nodo5 = Node(1, Node(1), Node(1))

    assert unival(nodo1) == 6
    assert unival(nodo2) == 2
    assert unival(nodo3) == 1
    assert unival(nodo4) == 4
    assert unival(nodo5) == 3


if __name__ == '__main__':
    main()