# List Slicing
# To make a new list from existing list


my_list = [56, 43, 12, 45, 62, 41, 16, 97, 34, -100]
#           0   1   2   3   4   5   6   7   8   9
#         -10  -9  -8  -7  -6  -5  -4  -3  -2   -1
#
#

# result = my_list[7:2:-1]
# result = my_list[::-1]
# result = my_list[-8:-5]
# result = my_list[-9:]
result = my_list[-4:-10:-1]
print(result)
