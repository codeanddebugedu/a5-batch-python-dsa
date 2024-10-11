"""
Enter a start number = 4
Enter a end number = 10

S to E

4 5 6 7 8 9 10
"""

start = int(input("enter start number = "))  # 4
end = int(input("enter end number = "))  # 10

i = start
while i <= end:
    print(i, end=" ")
    i += 1
