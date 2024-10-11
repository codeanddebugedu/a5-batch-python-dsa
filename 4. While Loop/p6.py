"""
Enter start = 3
Enter end = 87

Calculate sum of all the numbers divisible by 3 and 4
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
total = 0

i = start
while i <= end:
    if i % 3 == 0 and i % 4 == 0:
        total = total + i
    i += 1

print(total)
