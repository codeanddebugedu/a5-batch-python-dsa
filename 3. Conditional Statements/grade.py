"""
Ask a single mark from user

91 and above -> A
81-90 -> B
71-80 -> C
61-70 -> D
51-60 -> E
Fail
"""

mark = int(input("Enter marks = "))

if mark >= 91 and mark <= 100:
    print("A")
elif mark >= 81 and mark <= 90:
    print("B")
elif mark >= 71 and mark <= 80:
    print("C")
elif 61 <= mark <= 70:
    print("D")
elif mark >= 51 and mark <= 60:
    print("E")
elif mark >= 0 and mark <= 50:
    print("Fail")
else:
    print("Invalid")
