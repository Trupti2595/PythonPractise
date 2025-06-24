x = int(input("How much number: "))

n = 0
m = 1
count = 0

while count < x:
    print(n)
    nth = n + m
    n = m
    m = nth
    count +=1
