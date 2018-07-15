def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda p, q: p)


def cdr(pair):
    return pair(lambda p, q: q)


def car2(pair):
    def func(p, q):
        return p
    return pair(func)


def cdr2(pair):
    def func(p, q):
        return q
    return pair(func)


def main():
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))

    print(car2(cons(2, 5)))
    print(cdr2(cons(2, 5)))

if __name__ == '__main__':
    main()