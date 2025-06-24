# #WAp to input user's first name and print its length
# from itertools import count
#
# length = input("Enter user's frist name: ")
#
# print(len(length))
#
# # WAP to find an occurrence of '$' in a string
# str = "I $$$am T$rup$ti"
#
# print(str.count('$'))

# #WAP to check a number entered by user is odd or even
#
# num = int(input("Enter your number: "))
#
# if num%2 == 0:
#     print("Number entered is even")
# else:
#     print("Number entered is odd")

# #WAP to find the greatest of 3 numbers entered by the user
#
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))
#
# if a > b and a>c:
#     print(a)
# elif b>c:
#     print(b)
# else:
#     print(c)

#WAP to check if a number is multiple of 7 or not.
num = int(input("Enter any number: "))

if num%7 == 0:
    print(num, " is multiple of 7")
else:
    print(num, " is not multiple of 7")