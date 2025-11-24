#----------------------------------------Functions----------------------------------------
import random
from random import randint


def hello(name):
    print("Hello World " + name)

hello("Emir")

def sum_def(a,b,c):
    return a+b+c

def age(age= 18):
    print(age)
age(20)
age()

x = sum_def(2,3,7)
print(x)



#-------------------------------Arguments - Key Word Arguments------------------------------

def args_sum(*args):
  return sum(args)
print(args_sum(1,2,3,4,5,6,7,8,9,10))

def kwargs_example(**kwargs):
    print(kwargs)
kwargs_example(moscow = 100, berlin = 200 , roma = 300)


#-------------------------------------Practical Functions------------------------------------

def divide_number(num):
    return num / 2
myDivideList = [3,5,7,10,20,30]
resultList = []
for i in myDivideList:
    resultList.append(divide_number(i))

print(resultList)


#---------Map
print(list(map(divide_number, myDivideList)))

def string_control(string_con):
    return "a" in string_con
stringList = ["aab","bcd","akl","mam"]
stringResult  = map(string_control, stringList)
print(list(stringResult))

#---------Filter
resultFilter = filter(string_control, stringList)
print(list(resultFilter))


#---------Lambda
multiplyLambda = lambda num : num * 3
print(multiplyLambda(3))



#---------Scope
y = 10
def changeY():
    global y
    y = 5
    print(y)
changeY()
print(y)

#---------Palindrome Exercise

def isPalindrome(string):
    string = string.lower()
    return string[::-1] == string

while True:
    text = input("Enter a string: ")
    if text == "q":
        break
    print(isPalindrome(text))


#------Number Guess Exercise

pc_number = randint(1,100)
print(pc_number)
condition = ""

while True:
    user_guess = int(input(f"Enter a {condition} number: "))
    if user_guess > pc_number:
        condition = "lower"
    elif user_guess < pc_number:
        condition = "higher"
    else:
        print("Your guess is true")
        break









