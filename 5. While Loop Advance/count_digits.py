"""
ASk a number from user.

Count the number of digits
"""

from math import log10

num = int(input("Enter a number = "))
n = num
count = 0

while n > 0:
    count += 1
    n = n // 10

print(count)
print(int(log10(num)) + 1)
