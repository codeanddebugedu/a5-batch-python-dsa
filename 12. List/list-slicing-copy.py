my_list = [56, 43, 12, 45, 62, 41, 16, 97, 34, -100]
print(id(my_list))


# my_list.reverse()
# my_list = my_list[::-1] # Override
my_list[:] = my_list[::-1]
print(id(my_list))


print(my_list)
