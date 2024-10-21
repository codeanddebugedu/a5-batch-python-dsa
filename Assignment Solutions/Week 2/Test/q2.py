total = 0
count = 0
while True:
    num = int(input("Enter a number = "))
    if num == 0:
        break
    total += num
    count += 1
if count > 0:
    print(total / count)
else:
    print(0)
