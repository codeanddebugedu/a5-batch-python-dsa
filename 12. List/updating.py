my_list = [56, 43, 12, 34, 3, 7, 5, 43]

"""
Ask Index from user = -5
Enter a new value = 1
"""
my_list = [5, 6, 45, 3, 5, 6, 67, 4, 23, 11]
index = int(input("Enter a index = "))
new_value = int(input("Enter a new value = "))

n = len(my_list)
if index >= n or index < -n:
    print("Index does not exists")
else:
    my_list[index] = new_value

print(my_list)
