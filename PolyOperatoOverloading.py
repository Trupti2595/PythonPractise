# class ComplexNumber:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i
#     def __add__(self, other):
#         return f"{self.r + other.r} + {self.i + other.i}i"
#
#
# c1 = ComplexNumber(3, 3)
# c2 = ComplexNumber(4, 4)
# print(c1+c2)

class AgeCompare:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

p1 = AgeCompare("Trupti", 99)
p2 = AgeCompare("Sumit", 30)

if p1 > p2:
    print(p1.name, "will pay the bill")
else:
    print(p2.name, "will pay the bill")