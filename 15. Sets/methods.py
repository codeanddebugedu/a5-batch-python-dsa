my_set = {56, 44, "Anirudh", 99.66, "xyz", 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2}
my_set2 = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(100)
my_set.add(200)

print(my_set)

my_set.remove(56)
print(my_set)


print(my_set.union(my_set2))
print(my_set.intersection(my_set2))
