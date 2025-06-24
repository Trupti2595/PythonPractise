#Create student class that takes name and class of 3 subjects as arguments in constructor. Then create method to print objet
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        marks = 0
        for val in self.marks:
            marks = val + marks
        print("Hi, ",  self.name, "Your avg is: ",  marks/3)

    @staticmethod
    def hello():
        print("Hello")

s1 = Student("karan", [99, 98, 97])
s1.avg()

s1.name = "Sumit"
s1.avg()

s1.hello()