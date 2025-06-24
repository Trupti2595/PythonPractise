#Create class called order which stores item and its price
#user dunder function __gt__ to convey that: order1>order2 if price of order1>order2

class Order:
    def __init__(self, order1, order2):
        self.order1 = order1
        self.order2 = order2

    def __gt__(self):
        if self.order1 > self.order2:
            print("Order1 price is high")

o1 = Order(9500, 760)
o1.__gt__()