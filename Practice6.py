#Write a Python program that accepts the user's first and last name and prints them in reverse order
# with a space between them.

class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def reverse(self):
        print(self.lname, self.fname)

n1 = Name("Trupti", "Bansod")
n1.reverse()
print("************************************")

#Write a Python program to display the first and last colors from the following list.
class Colors:
    def __init__(self, colorslist):
        self.colorslist = colorslist

    def showColors(self):
        print(self.colorslist[0], self.colorslist[-1])


c1 = Colors(("Red", "Green", "White", "Black"))
c1.showColors()



