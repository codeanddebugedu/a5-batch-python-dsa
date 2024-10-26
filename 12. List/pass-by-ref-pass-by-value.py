"""
Pass by Reference/Address -> Only works for Mutable Objects
Pass by Value -> Only works for Immutable Objects
"""


def abcdef(my_list):
    print(x)
    print(id(my_list))
    my_list[0] = 110


# def jjjj(num):
#     num = 1000
#     print(id(num))


x = [4, 5, 6, 44, 5, 6, 411]
print(id(x))
abcdef(x)
print(x)

# x = 10
# print(id(x))
# jjjj(x)
# print(x)
