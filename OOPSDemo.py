#Classes and Objects

class Calculator:
    num = 100 #Class Variable
    def getdata(self):
        print("I am now executing as method in class")
obj = Calculator() #Syntax to create object in Python
obj.getdata()
print(obj.num)
print("**************************************************************")
#Constructor
class Greet:
    num1=200
    def __init__(self): #Construtor
        print("Good Morningggg, I called automatically when object is created")
    def getdata1(self):
        print("Good Morning, I am now executing as method in class")

obj1 = Greet()
obj1.getdata1()
print(obj1.num1)

print("**************************************************************")

#instance variable
class summmation:
    num2 = 500
    num1 = 300
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b

    def addnumbers(self):
        print("I am adding numbers")
        return self.firstnumber + self.secondnumber + summmation.num2

obje = summmation(2 , 3)
obje.addnumbers()
print(obje.addnumbers())

obje1 = summmation(6, 7)
obje1.addnumbers()
print(obje1.addnumbers())
