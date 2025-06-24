
greeting = 'Good Morning'

if greeting == 'Good Morning':
    print("True")
else:
    print("False")

#Loops
obje = [1, 2, 3, 4]
for i in obje:
    print(i)

print(" ")
for i in obje:
    print(i*2)

print(" ")

for j in range(1,6):
    print(j)
print(" ")
#sum of first 5 natural number 1+2+3+4+5 = 15
summation = 0
for j in range(1,6):
    summation = summation + j
    print(summation)
print(" ")

#skip some value in between
for k in range(1, 20, 5):
    print(k)
print(" ")

#if not passing 1 index, it will start from by default 0
for m in range(10):
    print(m)
