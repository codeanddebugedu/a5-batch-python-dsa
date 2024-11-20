class Student:

    # Magic Method
    def __init__(self, roll_no, name, age, gender, schoolname="XYZ"):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.schollname = schoolname

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


s1 = Student(1, "Anirudh", 22, "Male", schoolname="SDJ")
s1.display()


print(type(s1))
