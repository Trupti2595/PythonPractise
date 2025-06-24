
def enterexit(func):
    def enter():
        input("Enter your pin: ")
        func()
        print("Transaction completed....")
    return enter

@enterexit
def debit():
    print("Current amount after debit 200: ", 1000-200)

debit()

