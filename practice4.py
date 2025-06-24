#Define Employee class with attributes role, department and salary. this class also has a show details method
#Create an engineer class that inherits properties from Employee and has additional attributes name and age
from tkinter.font import names


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def details(self):
        print(self.role, self.department, self.salary)

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Tech", 90000)

eng = Engineer("Trupti Bansod", 30)
eng.details()


