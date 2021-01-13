
# This is a single line comment

"""
This is a multiline comment,
that takes up,
multiple lines
"""

# Prints "Hello" to the terminal
print("Hello")

"""
PRIMITIVE DATA TYPES
- integer (1, 2, 3)
- float (1.0, 1.5)
- string ("Hello", "Hi!", "40", "4.5")
- boolean (True, False)
"""

firstVariable = 5
print(firstVariable) #prints 5
print(type(firstVariable)) #prints <class 'int'>

secondVariable = 5.0
print(secondVariable) #prints 5.0
print(type(secondVariable)) #prints <class 'float'>

thirdVariable = "5"
print(thirdVariable) #prints 5
print(type(thirdVariable)) #prints <class 'str'>

fourthVariable = True
print(fourthVariable) #prints True
print(type(fourthVariable)) #prints <class 'bool'>

a = 5
b = 10
c = a + b
print(c) #prints 15
print(type(c)) #prints <class 'int'>

"""
ARITHMETIC OPERATORS
+
-
*
/
%
"""

# modulus (remainder when you divide)
d1 = 10%3
print(d1) #prints 1
d2 = 12%3
print(d2) #prints 0

e1 = 1
f1 = 2
g1 = e1 + f1
print(g1) #prints 3
print(type(g1)) #prints <class 'int'>

e2 = 1
f2 = 1.0
g2 = e2 - f2
print(g2) #prints 0.0
print(type(g2)) #prints <class 'float'>

h = 10
i = 3
j = h/i
print(j) #prints 3.333
print(type(j)) #prints <class 'float'>

k = "Hello!"
l = "Nice to meet you!"
m = k + l
print(m) #prints Hello!Nice to meet you!
print(type(m)) #prints <class 'str'>

o = 5
p = "Hello"
q = str(o) + p
print(q) #prints 5Hello
print(type(q)) #prints <class 'str'>

r1 = 5
s1 = "10"
t1 = r1 + int(s1)
print(t1) #prints 15
print(type(t1)) #prints <class 'int'>

r2 = 5
s2 = "10"
t2 = str(r2) + s2
print(t2) #prints 510
print(type(t2)) #prints <class 'str'>

"""
If statements/Conditions
"""
u = False
v = 7
w1 = 6
if (u):
    print("Hi!")
elif(v != w1):
    print("Blue!")
else:
    print("Pineapple!")

"""
COMPARISON OPERATORS
==
!=
< 
>
<=
>=
"""

"""
LOGICAL OPERATORS
and
or
not
"""

w2 = 12
x = 8
y = 9
z = 10

#Both conditions must be True
#prints "Hello"
if (x < y and y < z):
    print("Hello")

#Either of the conditions must be True
#prints "Hi"
if (x < y or w2 < z):
    print("Hi")

#Flips a condition to the opposite
#prints "Red"
aa = False
if(not aa):
    print("Red")

"""
LOOPS
for
while
"""

for i in range(5, 10):
    print("i", i)

bb = 1
while (bb < 10):
    print("bb", bb)
    bb = bb + 1
print("end of while loop")

"""
DATA STRUCTURES
list
set
dictionary
"""

"""
LISTS
maintains order of elements
"""
myList = []
myList.append("Apples") #adds element to the end of the list
myList.append("Apples")
myList.append("Apples")
myList.append("Eggs")
myList.append(1)
print(myList)
print(len(myList)) #prints number of elements in the list
print(myList[1]) #prints the 2nd element in the list
poppedOff = myList.pop() #removes last element in list
print(myList)
print(poppedOff) #prints the element removed from the end of the list

for i in range(len(myList)):
    print(myList[i])

#special loop for lists
for food in myList:
    print(food)

"""
SETS
cannot contain duplicate elements
"""
mySet = set()
mySet.add("Apples") #adds element to the set
mySet.add("Apples")
mySet.add("Apples")
mySet.add("Eggs")
mySet.add(True)
mySet.add(7)
print(mySet)
print(len(mySet)) #prints number of elements in the set
print("Grapes" in mySet) #prints True or False if the element is in the set
mySet.remove("Apples") #removes specific element from set
print(mySet)

"""
DICTIONARIES
key:value pairs
keys are all unique
"""
myDictionary = {}
myDictionary['apple'] = "pie" #add key:value pair to dictionary
myDictionary['happy'] = True
myDictionary['go'] = "bears"
myDictionary['blue'] = 42
print(myDictionary)
print('purple' in myDictionary) #prints True or False if the element is a key in the dictionary
print(myDictionary.keys()) #prints the keys of the dictionary
print(myDictionary.values()) #prints the values of the dictionary
del myDictionary['blue'] #removes specific key from set
print(myDictionary)


"""
FUNCTIONS
like rubber stamps of code that you can put in multiple places
"""
def sayHello():
    print("Hello")

sayHello() #function call that runs the code in the function definition
sayHello()
sayHello()
sayHello()

"""
Functions with Parameters
"""

def sayHi(name):
    print("Hi " + name)

sayHi("John") #prints Hi John
sayHi("April") #prints Hi April

def addition(a, b):
    print(a + b)

addition(1, 2) #prints 3
addition(3, 5) #prints 8

def hugs(a, b):
    print(a + " hugs " + b)

hugs("April", "John") #prints April hugs John
hugs("John", "April") #prints John hugs April




