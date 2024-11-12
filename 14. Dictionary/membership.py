# in and notin


details = {
    "name": "Anirudh",
    "physics": 80,
    "chemistry": 12,
    "english": 65,
    "abc": [1, 2, 2, 3, 3, 4, 4],
}


key = input("Enter a key = ")
if key in details:
    print(details[key])
else:
    print("Does not exists")
