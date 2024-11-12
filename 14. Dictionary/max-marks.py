# Print the maximum marks and also with name

details = {
    "Anirudh": [45, 65, 43, 11, 89],
    "Sanjay": [56, 45, 21, 11, 12],
    "Vandana": [45, 65, 43, 56, 32],
    "Muskan": [55, 12, 64, 11, 89],
    "Akshay": [21, 65, 43, 11, 78],
}

maxi_marks = float("-inf")
maxi_name = ""

for name, marks in details.items():
    total = 0
    for i in range(0, len(marks)):
        total = total + marks[i]
    # WE got the total of a particular student
    # maxi_marks = max(maxi_marks, total)
    if total > maxi_marks:
        maxi_name = name
        maxi_marks = total

print(maxi_name, maxi_marks)
