class BankDetails:

    def __init__(self):
        self.name = "Trupti Bansod"
        self._bankbalance = 80000
        self.__accountnum = 1234556678

    def accountnum(self):
        return self.__accountnum

    def accountnum1(self, number):
        self.__accountnum = number
        return number


    def show(self):
        print("Name: ", self.name, "Account Balance: ", self._bankbalance, "Account Number: ", self.__accountnum)

c1= BankDetails()
print(c1.accountnum())
print(c1.accountnum1(70000))
c1.show()

