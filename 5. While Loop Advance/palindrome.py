# Check if it is a palindrome

num = int(input("Enter a number = "))
n = abs(num)
ans = 0

while n > 0:
    ld = n % 10
    ans = (ans * 10) + ld
    n = n // 10

if ans == num:
    print("Yes it is a palindrome")
else:
    print("It is not a palindrome")
