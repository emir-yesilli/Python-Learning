
#----------------------------------------Lists----------------------------------------
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

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

#----------------------------------------Nested List----------------------------------------

myNestedList = [10,20,30, [40,50,60]]
print(type(myNestedList[3]))
print(myNestedList[3][0])

#----------------------------------------Dictionaries----------------------------------------
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()     Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	    Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary

myDictionary = {"Moscow": "Russia", "Berlin": "Germany"}
print(type(myDictionary))

print(myDictionary.keys())
print(myDictionary.values())

countries = list(myDictionary.values())
print(countries)

myDictionary["Roma"] = "Italy"
print(myDictionary)

# "Get" method gives a default value when the key is not exist
print(myDictionary.get("Moscoq", 0))

#Question: print 200 and 40
dictionary_practice = {"k1":10 , "k2": [10,20,30,40,50] , "k3": "string" , "k4": {"a": 100 , "b": 200}}
print(dictionary_practice["k4"]["b"])
print(dictionary_practice["k2"][3])


#----------------------------------------Sets----------------------------------------
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()		Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()		Returns a set, that is the intersection of two other sets
# intersection_update()		Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()		Returns True if all items of this set is present in another set
# issuperset()		Returns True if all items of another set is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()		Returns a set with the symmetric differences of two sets
# symmetric_difference_update()		Inserts the symmetric differences from this set and another
# union()		Return a set containing the union of sets
# update()		Update the set with the union of this set and others

set2 = {30,40,50,60,60}
set1 = {10,20,30,40}

print(set2)

print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))

print(set1.intersection(set2))

print(set1.union(set2))

print(set1.isdisjoint(set2))


set1.symmetric_difference_update(set2)
print(set1)

set1.discard(60)
print(set1)



#----------------------------------------Tuples----------------------------------------

#Does the same work as a list except it is immutable
myTuple = (10,20)
print(myTuple[1])

#   myTuple[0] = 100  --------> Error


#----------------------------------------Boolean----------------------------------------
#Mutable
isOk = True
print(type(isOk))
print(isOk)
isOk = False
print((isOk))

print(3>5)

#----------------------------------------------------------------------------------------
