file = open('DemoTest.txt')
#print(file.read())

#print(file.read(7)) #Read specific characters
# #Read by lines
#print(file.write('i'))

#Print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

file.close()

