num = int(input("Enter a number = "))
n = num
nod = 0
while n > 0:
    nod += 1
    n = n // 10
total = 0
n = num
while n > 0:

    ld = n % 10
    total = total + (ld**nod)
    n = n // 10
if total == num:
    print("Yes")
else:
    print("No")
