"""
n = 9

5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

# for i in range(5, 0, -1):
#     for j in range(5, i - 1, -1):
#         print(j, end=" ")
#     print()

# for i in range(2, 6):
#     for j in range(5, i - 1, -1):
#         print(j, end=" ")
#     print()

n = 9
for i in range(n // 2 + 1, 0, -1):
    for j in range(n // 2 + 1, i - 1, -1):
        print(j, end=" ")
    print()

for i in range(2, n // 2 + 1 + 1):
    for j in range(n // 2 + 1, i - 1, -1):
        print(j, end=" ")
    print()
