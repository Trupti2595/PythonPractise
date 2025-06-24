def start1(func):
    def startend1():
        print("Execution started")
        func()
        print("Execution completed")
    return startend1

@start1
def add1():
    print("Addition of 1st and 2nd number is ", 5+9)

add1()