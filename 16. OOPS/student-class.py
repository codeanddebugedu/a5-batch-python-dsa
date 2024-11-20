class Student:
    # Attributes/Class Variables
    # roll_no = 0
    # name = ""
    # age = 0
    # gender = ""

    # Magic Method
    def __init__(self):
        self.roll_no = int(input("Enter roll no = "))
        self.name = input("Enter name = ")
        self.age = int(input("Enter student age = "))
        self.gender = input("Enter student gender = ")

    # Methods
    def display(self):
        print(f"roll_no = {self.roll_no}")
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")

    # def update(self):
    #     self.name = input("Enter new student name = ")
    #     self.age = int(input("Enter new student age = "))

    def update(self, new_name=None, new_age=None):
        if new_name != None:
            self.name = new_name
        if new_age != None:
            self.age = new_age


s1 = Student()
s1.display()
print("--------")
# s1.update("Anirudh", 100)
s1.update(new_age=100, new_name="Sanjay")
print("--------")
s1.display()
