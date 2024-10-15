"""
ASk a number from user.

Count the number of digits
"""

num = int(input("Enter a number = "))
n = num
count = 0

while n > 0:
    count += 1
    n = n // 10

print(count)
