
a= 5 #Integer
b= 5.4 #float
c= 100+3j #complex
d= 'Sachin' #string


values = [1, 2, 'Trupti', 4.5, 5] #List
#List is the datatypes that allows multiple values and that can be different datatypes
print(values[0])
print(values[4])
print(values[-1]) #shortcut to last value
print(values[1:3]) #from to until(Last one will not be printed)
values.insert(3, "Bansod") #to insert values
print(values)
values.append("end") #to insert value at end
print(values)
values[2] = "TRUPTI" #Updating any value
print(values)
del values[0]
print(values)

val = (1, 2, "Values", 4.5) #Tuple

val1 = {'a':8, 5:'Trupti', 7:'Bansod'} #Dictionary
print(val1["a"])
print(val1[5])

#adding values in empty dictionary
dict= {}

dict["Firstname"] = "Trupti"
dict["Lastname"] = "Bansod"
dict["age"] = 29
print(dict)