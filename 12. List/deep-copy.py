from copy import deepcopy


lst1 = [1, 4, 6, "Anirudh", 44, 55, [98, 67, 64], 67, 87]


# lst2 = lst1.copy()  # Shallow Copy
lst2 = deepcopy(lst1)  # Deep Copy

print(f"Value of Lst1 = {lst1}")
print(f"ID of Lst1 = {id(lst1)}")
print(f"Value of Lst2 = {lst2}")
print(f"ID of Lst2 = {id(lst2)}")
print(id(lst1[6]))
print(id(lst2[6]))


lst2[6][1] = 100
print(f"Value of Lst1 = {lst1}")
print(f"Value of Lst2 = {lst2}")
