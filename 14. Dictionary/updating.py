details = {
    "name": "Anirudh",
    "physics": 80,
    "chemistry": 12,
    "english": 65,
    "abc": [1, 2, 2, 3, 3, 4, 4],
}

details["physics"] = 10  # If exists, then update
details["computer"] = 58  # If not exists, then add at last
details.update({"english": 100, "maths": 97, "abc": 99, "name": "Sanjay"})
print(details)


# del details["name"]
x = details.pop("name")
print(x)
print(details)
