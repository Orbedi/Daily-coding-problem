""" Problem:
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all
strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, tree, data):
        if tree is None:
            tree = Node(data)
        else:
            current = tree.value
            if current > data:
                tree.left = self.insert(tree.left, data)
            else:
                tree.right = self.insert(tree.right, data)
        return tree

    def search(self, tree, data, result):
        if tree is None:
            return
        else:
            if data == tree.value[0:len(data)]:
                result.append(tree.value)
                self.search(tree.left, data, result)
                self.search(tree.right, data, result)
            elif data < tree.value:
                self.search(tree.left, data, result)
            else:
                self.search(tree.right, data, result)


def prefix(list_, prfx):
    tree = Tree()
    for item in list_:
        tree.root = tree.insert(tree.root, item)
    result = []
    tree.search(tree.root, prfx, result)
    return result


if __name__ == '__main__':
    list_ = ['aaa', 'bbb', 'ccc', 'dog', 'deer', 'home', 'car', 'deal', 'aba', 'dezf']
    list_2 = ['ccc', 'bba', 'baa', 'dde', 'ddd']
    list_3 = ['ccc', 'cbba', 'cbaa', 'cdde', 'cddd']
    list_4 = []

    assert prefix(list_,'de') == ['deer', 'deal', 'dezf']
    assert prefix(list_2,'b') == ['bba', 'baa']
    assert prefix(list_3,'c') == ['ccc', 'cbba', 'cbaa', 'cdde', 'cddd']
    assert prefix(list_3,'cd') == ['cdde', 'cddd']
    assert prefix(list_4,'prueba') == []

