"""
Enter start = 3
Enter end = 50

Print numbers divisble by 2 and 7 
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
i = start
while i <= end:
    if i % 2 == 0 and i % 7 == 0:
        print(i, end=" ")
    i += 1
