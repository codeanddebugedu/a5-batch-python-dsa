details = {
    "name": "Anirudh",
    "physics": 80,
    "chemistry": 12,
    "english": 65,
    "abc": [1, 2, 2, 3, 3, 4, 4],
}


# x = details.copy()
# details.clear()

k = input("Enter a key = ")
if details.get(k) != None:
    print(details[k])
else:
    print("Key does not exists")
