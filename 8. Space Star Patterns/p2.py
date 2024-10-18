n = 5
for i in range(5, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(5, i - 1, -1):
        print(k, end=" ")
    print()
