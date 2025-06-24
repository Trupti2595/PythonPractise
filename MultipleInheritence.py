# class Addition:
#     def add(self):
#         add1=self.a + self.b
#         return add1
#
# class Substraction:
#
#     def sub(self):
#         sub1 = self.a - self.b
#         return sub1
#
# class Show(Addition, Substraction):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def printing(self):
#         addition = Addition.add(self)
#         substration = Substraction.sub(self)
#         print("Ans for Addtion:", addition,  "Ans of Substraction: ", substration)
#
# c = Show(46, 42)
# c.printing()


class Addition():
    def add(self):
        add1 = self.a + self.b
        return add1

class Subtraction():
    def sub(self):
        sub1 = self.a - self.b
        return sub1

class Show(Addition, Subtraction):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def printint(self):
        print("Result of Addition: ", self.add())
        print("Result of Subtraction: ", self.sub())

c1 =  Show(5, 2)
c1.printint()













