# Ascii Values

s = "hjfhes74392&^*(^nkdnakhlk789743)"

n = len(s)
count = 0

# for i in range(0, n):
#     ascii_value = ord(s[i])
#     if ascii_value >= 97 and ascii_value <= 122:
#         count += 1

for i in range(0, n):
    # if "a" <= s[i] <= "z":
    if s[i] >= "a" and s[i] <= "z":
        count += 1


print(count)
