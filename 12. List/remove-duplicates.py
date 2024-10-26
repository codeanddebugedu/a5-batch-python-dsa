def remove_duplicates(my_list):
    result = []
    n = len(my_list)
    for i in range(0, n):
        if my_list[i] not in result:
            result.append(my_list[i])
    return result


lst = [5, 6, 4, 4, 4, 2, 3, 3, 7, 7, 9, 1, 2, 1]
new_list = remove_duplicates(lst)
print(new_list)
