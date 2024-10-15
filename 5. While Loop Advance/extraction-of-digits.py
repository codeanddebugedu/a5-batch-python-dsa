num = int(input("Enter a number = "))
# n = abs(num)
if num < 0:
    n = num * -1
else:
    n = num

while n > 0:
    ld = n % 10
    print(ld)
    n = n // 10
