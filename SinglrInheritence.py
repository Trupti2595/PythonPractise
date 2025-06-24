class Addition:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print("Addition of 2 numbers: ", self.a + self.b)

class Substraction(Addition):

    def sub(self):
        print("Substraction of 2 numbers: ", self.a-self.b)


s1 = Addition(55, 45)
s1.addition()
s2 = Substraction(95, 85)
s2.sub()
