class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Grade:", self.calculate_grade())

s1 = Student("Dhruv", 101, 88)
s1.display()