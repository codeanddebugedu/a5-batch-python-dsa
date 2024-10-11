"""
1 to 100

Count the numbers which are divisble by 7
"""

count = 0

i = 1
while i <= 100:
    if i % 7 == 0:
        count = count + 1
    i += 1

print(count)
