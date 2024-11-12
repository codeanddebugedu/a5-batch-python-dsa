# To access all keys or values or both

details = {
    "name": "Anirudh",
    "physics": 80,
    "chemistry": 80,
    "english": 80,
}
print(details.items())

for k, v in details.items():
    print(f"k={k}       v={v}")

# for k in details.keys():
#     print(k, details[k])

# for k in details:
#     print(k, details[k])

# for v in details.values():
#     print(v)
