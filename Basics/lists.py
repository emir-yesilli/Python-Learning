
#--------------------Lists--------------------

myList = [10,20,30,40,50,60,70]
secondList = [1,2,3,4,5,6]
print(type(myList))

print(myList[0])
print(myList[-1])
print(myList[:3])
print(myList[::2])
print(max(myList))
print(min(myList))

myList.append(80)
print(myList)

myList.remove(10)
print(myList)

myList.count(20)
print(myList)

myList.extend(secondList)
print(myList)

myList.sort()
print(myList)

myList.sort(reverse=True)
print(myList)

myList.pop(0)
print(myList)

del myList[0]
print(myList)

print(myList.index(1))

#--------------------Nested List--------------------
myNestedList = [10,20,30, [40,50,60]]
print(type(myNestedList[3]))
print(myNestedList[3][0])