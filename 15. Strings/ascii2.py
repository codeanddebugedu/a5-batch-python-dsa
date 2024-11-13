s = "hjakwhd^&*#($^#      ^!&^&*ghcjkeagGDHWAGD83648GDWHAJDG)"


n = len(s)
small = 0
capital = 0
spaces = 0
symbol = 0
for i in range(0, n):
    ascii_value = ord(s[i])
    if ascii_value >= 97 and ascii_value <= 122:
        small += 1
    elif ascii_value >= 65 and ascii_value <= 90:
        capital += 1
    elif ascii_value == 32:
        spaces += 1
    else:
        symbol += 1


print(small)
print(capital)
print(spaces)
print(symbol)
