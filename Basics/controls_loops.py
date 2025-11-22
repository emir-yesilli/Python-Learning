#----------------------------------------If Controls----------------------------------------
from fontTools.voltLib.ast import Range

print(1==1)
print(1==2)
print(1 >= 0)
print(1 <= 0)

myList = [1,2,3,4,5]
print(1 in myList)
print(6 not in myList)

print(1>0 or 2 >3)
print(1>0 and 2>3)


myDictionary = {'a':1,'b':2,'c':3}
print("a" in myDictionary)
print(1 in myDictionary.values())


# ---Indentation is essential

# number = float(input("Enter a number: "))
# if number % 2 == 0:
#     print("Your number is even")
# elif number % 2 == 1:
#     print("Your number is odd")
# else:
#     print("Your number is not an integer")


#----------------------------------------Loops----------------------------------------
loopList = [10,20,30,40,50]
for x in loopList:
    print(x/5)




#------Pyramid Exercise
loopInt = int(input("Enter a odd number: "))

for z in range(loopInt):
 if loopInt-2*z <= 0:
     break
 print(" "* z +"*"*(loopInt-2*z))
 if loopInt-2*z <= 0:
     break

for i in range(int((loopInt+1)/2)):
 print(" " * int(((loopInt-1)/2)-i) + "*" * (2*i+1) )




#-----Diamond Exercise
for k in range(loopInt):
    space = abs((loopInt//2)-k)
    print(" " * space + "*" * (loopInt - 2 * space))



#----- Reverse Diamond Exercise
for m in range(loopInt):
    space = abs((loopInt // 2) - m)


    if m == 0 or m == loopInt -1:
        print(" " * space + "*" )
    else:
        space_inner = loopInt - (2 * space) - 2
        print(" "* space + "*" + " " * space_inner + "*")
