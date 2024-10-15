# Reverse a number

num = int(input("Enter a number = "))
n = abs(num)
ans = 0

while n > 0:
    ld = n % 10
    # print(ld, end=" ")
    ans = (ans * 10) + ld
    n = n // 10

print(ans)


print("Hey1")
print("Hey1")
print("Hey1")
print("Hey1")
