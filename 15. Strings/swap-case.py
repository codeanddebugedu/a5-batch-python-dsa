s = "ahnirud$#$#HDKJWA....642842dgwakh^&*^$#*^()"

"""
Small letter -> Upper
Upper letter -> Small
"""
n = len(s)

result = ""

for i in range(0, n):
    ascii_value = ord(s[i])
    if ascii_value >= 97 and ascii_value <= 122:
        new_ascii_val = ascii_value - 32
        new_ch = chr(new_ascii_val)
        result = result + new_ch
    elif ascii_value >= 65 and ascii_value <= 90:
        new_ascii_val = ascii_value + 32
        new_ch = chr(new_ascii_val)
        result = result + new_ch
    else:
        result = result + s[i]

print(result)
