num = int(input("Enter a number = "))
n = abs(num)
total = 0

while n > 0:
    ld = n % 10
    total = total + ld
    n = n // 10

print(total)
