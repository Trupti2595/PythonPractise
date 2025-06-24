class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Details(Employee):

    def hobbydetails(self):
        print("You age is:", self.age)

class Name(Details):
    def fetchdetails(self):
        print("Hello, My name is ", self.name, "My age is ", self.age)

N1 = Name("Trupti", 30)
N1.fetchdetails()


