# List Slicing -> O(k)
# To make a new list from existing list


my_list = [56, 43, 12, 45, 62, 41, 16, 97, 34, -100]
#           0   1   2   3  4    5   6   7   8   9
#
#
# result = []
# for i in range(3, 8):
#     result.append(my_list[i])
# result = my_list[3:8]
# result = my_list[0:7]
# result = my_list[0:7:2]
# result = my_list[4:]
# result = my_list[:]
result = my_list[::2]
print(result)
