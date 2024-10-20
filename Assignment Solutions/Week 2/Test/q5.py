# Not the most optimal solution
"""
start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
"""


# Most optimal solution 👇
import math

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=", ")
