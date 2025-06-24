class Main:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def result(self):
        if (self.a and self.b == int):
            print("Addition: ", self.a+self.b)
        elif (self.a and self.b == str):
            print("Number of times: ", self.a + self.b)
        else:
            print("Merge: ", self.a + self.b)

c1 = Main("Trupti", "Bansod")
c1.result()
