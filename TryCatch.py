#Try
#Manually added error
try:
    with open('emotest.txt' , 'r') as reader:
        reader.readline()
except:
     print("Somehow I reached this block because there is failure in try block")


print("****************************************************************************")


#Fetch the error what Python throws
try:
    with open('Dmotest.txt', 'r') as reader:
        reader.readline()
except Exception as e:
    print(e)
finally: #Finally: no matter if it is pass or fail in try block, finally will execute everytime
    print("Cleaning up resource")
