"""
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
"""

for i in range(1, 6):
    for j in range(1, 5 - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(k, end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(1, 5 - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(k, end=" ")
    print()
