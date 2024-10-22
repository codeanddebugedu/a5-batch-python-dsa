"""
Use 3 parameters

add(a,b,c)
sub(a,b,c)
mul(a,b,c)
"""


def add(n1: int, n2: int, n3: int):
    total = n1 + n2 + n3
    print(total)


def sub(n1: int, n2: int, n3: int):
    total = n1 - n2 - n3
    print(total)


def mul(n1: int, n2: int, n3: int):
    total = n1 * n2 * n3
    print(total)


a = 10
b = 30
c = 40
add(a, b, c)
sub(a, b, c)
mul(a, b, c)
