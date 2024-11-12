"""
Anirudh is of 45 age and gender is Male
Anirudh is of 45 age and gender is Male
Anirudh is of 45 age and gender is Male
"""

info = {
    "Anirudh": {"age": 45, "gender": "Male"},
    "Sanjay": {"age": 12, "gender": "Male"},
    "Vandana": {"age": 67, "gender": "Female"},
    "Muskan": {"age": 54, "gender": "Female"},
    "Akshay": {"age": 77, "gender": "Male"},
}

for name, details in info.items():
    print(f"{name} is of {details['age']} age and gender is {details['gender']}")
    # print(details.keys())
