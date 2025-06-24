class Parent:
    def sleep(self):
        print("My sleep time is 10PM to 5 AM")
    def eat(self):
        print("I love Punjabi cuisine")
    
class Son(Parent):
    def sleep(self):
        print("My sleep time is 1AM to 10AM")

    def eat(self):
        print("I love Chinese cuisine")

c1 = Parent()
c1.sleep()