"""
Immutable
Which cannot be changed at the same address
int, str, float, tuple

Mutable
Which can be changed at the same address
list, dictionary, set
"""

# a = 5
# print(f"Value of a = {a}")
# print(f"Address of a = {id(a)}")


# a = 10
# print(f"Value of a = {a}")
# print(f"Address of a = {id(a)}")

my_list = [56, 43, 12, 34, 3, 7, 5, 43]
print(my_list)
print(id(my_list))

my_list[2] = 99999
my_list[-1] = 100
print(my_list)
print(id(my_list))


my_list = [1, 2, 3]  # New List is assigned
print(my_list)
print(id(my_list))
