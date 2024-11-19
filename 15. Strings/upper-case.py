"""
s= aniRUdh


ANIRUDH
"""

s = "anirudh$#$#HDKJWA642842dgwakh^&*^$#*^()"
n = len(s)

result = ""

for i in range(0, n):
    ascii_value = ord(s[i])
    if ascii_value >= 97 and ascii_value <= 122:
        new_ascii_val = ascii_value - 32
        new_ch = chr(new_ascii_val)
        result = result + new_ch
    else:
        result = result + s[i]

print(result)
