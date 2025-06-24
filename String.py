string = "Trupti Bansod"
string1 = "Trupti"
string2 = "    truptibansod19@gmail.com    "
print(type(string))

print(string[0])
print(string[1])
print(string[7])
print(string[0:6])
print(string + " " + string1)

print(string1 in string)

print(string2.split("@"))
print(string2.strip()) #Trimming beginnin and last white spaces
print(string2.lstrip())
print(string2.rstrip())