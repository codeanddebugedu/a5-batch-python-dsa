"""
Scope
    1. Local Variable
    2. Global Variable
"""


def abcdefg():
    # global a
    # global b
    a = 200
    b = 1000
    print(id(a))
    print(id(b))


a = 10
b = 20
print(a, b)
print(id(a))
print(id(b))
abcdefg()
print(a, b)
