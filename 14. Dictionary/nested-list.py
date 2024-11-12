"""
Anirudh has scored 323 marks
Sanjay has scored 121 marks
"""

details = {
    "Anirudh": [45, 65, 43, 11, 89],
    "Sanjay": [56, 45, 21, 11, 12],
    "Vandana": [45, 65, 43, 56, 32],
    "Muskan": [55, 12, 64, 11, 89],
    "Akshay": [21, 65, 43, 11, 78],
}


# for name, marks in details.items():
#     total = sum(marks)
#     print(f"{name} has scored {total} marks")

for name, marks in details.items():
    total = 0
    for i in range(0, len(marks)):
        total = total + marks[i]
    print(f"{name} has scored {total} marks")
