"""
Enter a start number = 10
Enter a end number = 5

S to E

10 9 8 7 6 5
"""

start = int(input("Enter start number = "))  # 10
end = int(input("Enter end number = "))  # 3

i = start
while i >= end:
    print(i, end=" ")
    i -= 1
