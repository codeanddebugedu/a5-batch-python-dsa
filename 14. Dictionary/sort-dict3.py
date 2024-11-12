details = {
    "Anirudh": [45, 65, 43, 11, 89],
    "Sanjay": [56, 45],
    "Vandana": [45, 65, 43, 56, 32, 55, 66, 77],
    "Muskan": [55, 12, 64, 11, 89],
    "Akshay": [21, 65, 43, 11, 78],
}

# print(details.items())


# print(dict(sorted(details.items(), key=lambda x: x[1][4])))
# print(dict(sorted(details.items(), key=lambda x: x[1][-1])))
print(dict(sorted(details.items(), key=lambda x: sum(x[1]))))
