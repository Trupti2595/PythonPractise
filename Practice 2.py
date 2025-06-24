#Create account class with 2 attributes: balance and account no
#Create methods for debit, credit and printing the balance
from selenium.webdriver.common.devtools.v129.web_authn import add_credential


class Account:

    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs ", amount, "was debitted")
        print("Total Balance is: ", self.displayamount())

    def credit(self, amount):
        self.balance += amount
        print("Rs ", amount, "was creditted")
        print("Total Balance is: ", self.displayamount())

    def displayamount(self):
        return self.balance


ac1 = Account(4000, 3245696)
ac1.debit(1000)
ac1.credit(2000)
ac1.displayamount()

