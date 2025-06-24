# # def greet():
# #     print("Hello World")
#
# class Public:
#     def __init__(self):
#         self.name = "John"  # Public attribute
#
#     def display_name(self):
#         print(self.name)  # Public method
#
# obj = Public()
# obj.display_name()  # Accessible
# # print(obj.name)  # Accessible

numbers = [34, 66, 78]

for num in numbers:
    digit_sum = (num // 10) + (num % 10)
    if digit_sum % 2 == 0:
        print(num)
    else:
        continue