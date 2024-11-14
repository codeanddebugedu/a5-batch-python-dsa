"""
You need to make a string.

Enter char = a
Enter char = !
Enter char = 9
Enter char = b
Enter char = c
Enter char = q/Q

a!9bc
"""

s = ""

while True:
    ch = input("Enter a char = ")
    if ch == "q" or ch == "Q":
        break
    s = ch + s

print(s)
