#Inheritence
from OOPSDemo import summmation

class inheritence(summmation):

    def __init__(self):
        summmation.__init__(self, 5, 2)

    def getinterface(self):
        return self.num2 + self.num1 + self.addnumbers()

obe = inheritence()
obe.getinterface()
print(obe.getinterface())