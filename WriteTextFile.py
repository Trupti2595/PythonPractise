#Read the file and store all the line in list
#reverse the list
#Write the list back to the file

with open('DemoTest.txt', 'r') as reader: #This will open and close file so need not to write close() command in another line
    content = reader.readlines()
    #reversed(content)
    with open('DemoTest.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

