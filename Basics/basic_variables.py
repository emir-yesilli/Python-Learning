
#---------------------Variables---------------------

#Integer
age = 18

#String
name = "emir yeşilli"

#Bool
ok = True

#Float
pi = 3.14


print(type(age))
print(type(name))
print(type(ok))
print(type(pi))
print(age + 5)
print(age/3)

#Only integer value
print(age//4)

#Remainder
print(age%3)

#Exponential expression
print(age**2)

#-------------------------Strings-----------------------------

print(name.capitalize())
print(name.find("i"))
print(name.lower())
print(name.upper())
print(name.title())
print(name.replace("i","j"))
print(name.count("i"))
print(name.center(40))
print(name[0])
print(len(name))
print("emir" in name)

#   name[starting index : stopping index : stepping size]
print(name[:4])
print(name[4:])
print(name[-3:-1])
print(name.encode())
print(name[3::])
print(name[:3:])
print(name[::2])


#--------------------Converting Variables--------------------

myInteger = 20
myString = "30"
myList = ["10","20"]

print(str(myInteger))
print(int(myString))
print(float(myInteger))
print(int(myList[0])*2)
