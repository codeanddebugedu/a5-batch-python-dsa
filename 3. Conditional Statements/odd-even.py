"""
Ask a number

EVen
ODD
"""

# num = int(input("Enter a number = "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Yes, if number divisible by 2, 6 but 12 divisible
num = 18
if num % 2 == 0 and num % 6 == 0 and num % 12 != 0:
    print("YEs")
else:
    print("No")
