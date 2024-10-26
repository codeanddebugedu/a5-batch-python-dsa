lst1 = [5, 64, 5, 6, 8, 7, 8, 7]
lst2 = lst1.copy()  # Shallow Copy

print(f"Value of Lst1 = {lst1}")
print(f"ID of Lst1 = {id(lst1)}")
print(f"Value of Lst2 = {lst2}")
print(f"ID of Lst2 = {id(lst2)}")


lst2[-1] = 100
print(f"Value of Lst1 = {lst1}")
print(f"ID of Lst1 = {id(lst1)}")
print(f"Value of Lst2 = {lst2}")
print(f"ID of Lst2 = {id(lst2)}")
