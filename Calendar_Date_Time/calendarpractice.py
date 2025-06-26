# Write a Python program that takes a year as input
# and prints whether it is a leap year or not using the calendar module.
import calendar


year = int(input("Enter Year: "))
if calendar.isleap(year):
    print("Leap Year")
else:
    print("it is not leap year")

