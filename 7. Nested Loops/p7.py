# n = 6
# for i in range(1, n // 2 + 1 + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# for i in range(n // 2, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
n = 6
for i in range(1, n // 2 + 1 + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()

for i in range(n // 2, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()
