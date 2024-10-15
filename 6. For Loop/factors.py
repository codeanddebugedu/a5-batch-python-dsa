"""
You will be given a number

num = 10
1 2 5 10

num = 25
1 5 25

num = 100
1 2 4 5 10 20 25 50 100
"""

# Method 1
# num = 100
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, end=" ")

# Method 2
# num = 100
# for i in range(1, num // 2 + 1):
#     if num % i == 0:
#         print(i, end=" ")
# print(num)

num = 100
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        print(i)
        if num // i != i:
            print(num // i)
