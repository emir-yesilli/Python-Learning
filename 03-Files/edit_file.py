myFile = open('text.txt')
print(type(myFile))

print(myFile.read())
print(myFile.read())

myFile.seek(0)
print(myFile.read())

# w --> Write , r --> Read , a --> Append

with open('text.txt', mode = "w") as myFile:
    myFile.write("test 4")
with open ('text.txt', mode = "r") as myFile2:
    print(myFile2.read())
with open('text.txt', mode = "a") as myFile3:
    myFile3.write('\n'+"test 5" )
with open ('text.txt', mode = "r") as myFile4:
    print(myFile4.read())
