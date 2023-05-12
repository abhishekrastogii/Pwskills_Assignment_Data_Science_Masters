#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to illustrate a list

# creates a empty list
nums = []

# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")

print(nums)


# In[2]:


# Python code to demonstrate working of keyword()

# importing "keyword" for keyword operations
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)


# #The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.
# 
# The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.

# In[4]:


# showing logical operation
# or (returns True)
print(True or False)

# showing logical operation
# and (returns False)
print(False and True)

# showing logical operation
# not (returns False)
print(not True)

# using "in" to check
if 's' in 'geeksforgeeks':
	print("s is part of geeksforgeeks")
else:
	print("s is not part of geeksforgeeks")

# using "in" to loop through
for i in 'geeksforgeeks':
	print(i, end=" ")

print("\r")

# using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' '  is  ' ')

# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({}  is  {})


# In[8]:


# Using for loop
for i in range(10):

	print(i, end=" ")

	# break the loop as soon it sees 6
	if i == 6:
		break
print()

# loop from 1 to 10
i = 0
while i < 10:

	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 6:
		i += 1
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end=" ")

	i += 1


# In[9]:


# Return keyword
def fun():
	S = 0

	for i in range(10):
		S += i
	return S


print(fun())

# Yield Keyword


def fun():
	S = 0

	for i in range(10):
		S += i
		yield S


for i in fun():
	print(i)


# In[10]:


# Python3 program to
# demonstrate instantiating
# a class


class Dog:

	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()


# In[11]:


import math as gfg

print(gfg.factorial(5))


# In[12]:


# using with statement
with open('file_path', 'w') as file:
	file.write('hello world !')


# In[13]:


n = 10
for i in range(n):

	# pass can be used as placeholder
	# when code is to added later
	pass


# In[14]:


# Lambda keyword
g = lambda x: x*x*x

print(g(7))


# In[15]:


# import keyword
from math import factorial
import math
print(math.factorial(10))

# from keyword
print(factorial(10))


# In[16]:


# initializing number
a = 4
b = 0

# No exception Exception raised in try block
try:
	k = a//b # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')

# assert Keyword
# using assert to check for 0
print("The value of a / b is : ")
assert b != 0, "Divide by 0 error"
print(a / b)

# raise keyword
# Raises an user defined exception
# if strings are not equal
temp = "geeks for geeks"
if temp != "geeks":
	raise TypeError("Both the strings are different.")


# In[1]:


# Python program showing how to
# multiple input using split

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

# taking two inputs at a time
a, b = input("Enter two values: ").split()
print(f"First number is {a} and second number is {b}")

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int,input("Enter multiple values: ").split()))
print("List of students: ", x)


# In[27]:


import time

count_seconds = 10
for i in reversed(range(count_seconds + 1)):
	if i > 0:
		print(i, end='>>>')
		time.sleep(1)
	else:
		print('Start')


# In[26]:


import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
	if i > 0:
		print(i, end='>>>', flush = True)
		time.sleep(1)
	else:
		print('Start')


# In[6]:


# Python program to illustrate
# math module
import math
a = math.fabs(-85.000)
print(a)


# In[1]:


# Examples of Arithmetic Operator
a = 9
b = 4
add = a + b
sub = a - b
mul = a * b
mod = a % b
p = a ** b
print(add)
print(sub)
print(mul)
print(mod)
print(p)


# In[2]:


# Examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)


# In[3]:


# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)


# In[4]:


# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)


# In[5]:


# Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)


# In[6]:


# identity operator
a = 10
b = 20
c = a

print(a is not b)
print(a is c)


# In[7]:


# Python program to illustrate
# not 'in' operator
# membership operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
	print("x is NOT present in given list")
else:
	print("x is present in given list")

if (y in list):
	print("y is present in given list")
else:
	print("y is NOT present in given list")


# In[4]:


# Program to demonstrate conditional operator
a, b = 20,10

# Copy value of a in min if a < b else copy b
min = a if a > b else b

print(min)


# In[5]:


# Examples of Operator Precedence

# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)

# Precedence of 'or' & 'and'
name = "Alex"
age = 0

#### please note

if name == "Alex" or name == "John" and age >= 2:
	print("Hello! Welcome.")
else:
	print("Good Bye!!")
# if ((name == "Alex" or name == "John") and age >= 2):
# 	print("Hello! Welcome.")
# else:
# 	print("Good Bye!!")


# In[11]:


# Examples of Operator Associativity

# Left-right associativity
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)
print(100 / 10 * 10)

# Left-right associativity
# 5 - 2 + 3 is calculated as
# (5 - 2) + 3 and not
# as 5 - (2 + 3)
print(5 - 2 + 3)

# left-right associativity
print(5 - (2 + 3))

# right-left associativity
# 2 ** 3 ** 2 is calculated as
# 2 ** (3 ** 2) and not
# as (2 ** 3) ** 2
print(2 ** 3 ** 2)


# In[6]:


# A sample use of increasing the variable value by one.
count=0
count+=1
count=count+1
print('The Value of Count is',count)

# A Sample Python program to show loop (unlike many
# other languages, it doesn't use ++)
# this is for increment operator here start = 1,
# stop = 5 and step = 1(by default)
print("INCREMENTED FOR LOOP")
for i in range(5):
    print(i)

# this is for increment operator here start = 5,
# stop = -1 and step = -1
print("\n DECREMENTED FOR LOOP")
for i in range(4, -1, -1):
    print(i)
# for variable_name in range(start, stop, step)


# In[7]:


# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
# if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print
print( (a, b) [a < b] )

# Use Dictionary for selecting an item
# if [a < b] is true then value of True key will print
# else if [a<b] is false then value of False key will print
print({False: b,True: a} [a < b])

# lambda is more efficient than above two methods
# because in lambda we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())


# In[8]:


# Python program to demonstrate nested ternary operator
a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")


# In[21]:


# Python program to demonstrate nested ternary operator
a, b = 10, 20

if a != b:
	if a > b:
		print("a is greater than b")
	else:
		print("b is greater than a")
else:
	print("Both a and b are equal")


# In[22]:


a=5
b=7

# [statement_on_True] if [condition] else [statement_on_false]

print(a,"is greater") if (a>b) else print(b,"is Greater")


# In[23]:


# Define the data to be evaluated
data = [3, 5, 2, 8, 4]
# Use a for loop to evaluate each element in the data
for i in data:
    result = "even" if i % 2 == 0 else "odd"
    print(f"The number {num} is {result}")


# In[24]:


# Program to demonstrate conditional operator
a, b = 10, 20

# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't
# work if a is 0.
min = a < b and a or b

print(min)


# In[25]:


class MyClass:
	def __init__(self, value):
		self.value = value

	def __truediv__(self, other):
		return MyClass(self.value and other.value)

a = MyClass(True)
b = MyClass(False)
c = a / b # c.value is False


# In[11]:


# Program to reverse a string

gfg = "geeksforgeeks"

# Reverse the string using reversed and join function
gfg = "".join(reversed(gfg))

print(gfg)


# In[29]:


# Program to reverse a string

gfg = "geeksforgeeks"

# Reverse the string using reversed and join function gfg = reversed(gfg)
gfg.reverse()##--->>>>> this will only work for list
print(gfg)


# In[30]:


#Program to reverse a string
gfg = "geeksforgeeks"
print(gfg[::-1])


# In[37]:


# Python Program to Update
# character of a String
s= "Hello"
print("Initial String:")
print(s)
l=list(s)
l[2] = 'p'
S2= ''.join(l)
print("\nUpdating character at 2nd Index: ")
print(S2)
String3 = s[0:2] + 'p' + s[3:]
print(String3)


# In[38]:


# Python Program to Update
# entire String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a String
String1 = "Welcome to the Geek World"
print("\nUpdated String: ")
print(String1)


# In[39]:


# Python Program to Delete
# characters from a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a character
# of the String
String2 = String1[0:2] + String1[3:]
print("\nDeleting character at 2nd Index: ")
print(String2)


# In[40]:


# Python Program to Delete
# entire String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a String
# with the use of del
del String1
print("\nDeleting entire String: ")
print(String1)


# In[41]:


# Python Program for
# Escape Sequencing
# of String

# Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ")
print(String1)

# Escaping Single Quote
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ")
print(String1)

# Escaping Double Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)

# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)

# Printing Paths with the
# use of Tab
String1 = "Hi\tGeeks"
print("\nTab: ")
print(String1)

# Printing Paths with the
# use of New Line
String1 = "Python\nGeeks"
print("\nNew Line: ")
print(String1)


# In[14]:


# Printing hello in octal
String1 = "\110\145\154\154\157"
print("\nPrinting in Octal with the use of Escape Sequences: ")
print(String1)

# Using raw String to
# ignore Escape Sequences
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ")
print(String1)

# Printing Geeks in HEX
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1)

# Using raw String to
# ignore Escape Sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)


# In[43]:


# Python Program for
# Formatting of Strings

# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)


# In[44]:


# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)


# In[45]:


# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks",
													2009)
print(String1)


# In[49]:


# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map,
# split and strip functions
lst = list(map(int, input("Enter the integer\elements:").strip().split()))[:n]

# printing the list
print('The list is:', lst)


# In[50]:


# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)


# In[51]:


# Reversing a list
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)


# In[52]:


# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)
# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)


# In[53]:


# Creating a List
List = [1, 2, 3, 4, 5, 6,
		7, 8, 9, 10, 11, 12]
# Removing elements from List
# using iterator method
for i in range(1, 5):
	List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)


# In[54]:


List = [1, 2, 3, 4, 5]

# Removing element from the
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)

# Removing element at a
# specific location from the
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)


# In[55]:


# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List = ['G', 'E', 'E', 'K', 'S', 'F',
		'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List)

# Print elements of a range
# using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

# Print elements from a
# pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th "
	"element till the end: ")
print(Sliced_List)

# Printing elements from
# beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)


# In[56]:


# Creating a List
List = ['G', 'E', 'E', 'K', 'S', 'F',
		'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List)

# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)

# Print elements of a range
# using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)


# In[57]:


# Python program to demonstrate list
# comprehension in Python

# below list contains square of all
# odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)


# In[58]:


# for understanding, above generation is same as,
odd_square = []

for x in range(1, 11):
	if x % 2 == 1:
		odd_square.append(x**2)

print(odd_square)


# In[59]:


# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# In[60]:


# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	
	newList[0], newList[-1] = newList[-1], newList[0]

	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))


# In[61]:


# Python3 program to illustrate
# the usage of * operand
list = [1, 2, 3, 4]

a, *b, c = list

print(a)
print(b)
print(c)


# In[62]:


# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
	
	start, *middle, end = list
	list = [end, *middle, start]
	
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# In[63]:


# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
	
	first = list.pop(0)
	last = list.pop(-1)
	
	list.insert(0, last)
	list.append(first)
	
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# In[64]:


# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)


# In[65]:


# Creating a Tuple
# with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

# Creating a Tuple
# with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# Creating a Tuple
# with repetition
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

# Creating a Tuple
# with the use of loop
Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
	Tuple1 = (Tuple1,)
	print(Tuple1)


# In[66]:


# Accessing Tuple
# with Indexing
Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple1[0])


# Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")

# This line unpack
# values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)


# In[67]:


# Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')

Tuple3 = Tuple1 + Tuple2

# Printing first Tuple
print("Tuple 1: ")
print(Tuple1)

# Printing Second Tuple
print("\nTuple2: ")
print(Tuple2)

# Printing Final Tuple
print("\nTuples after Concatenation: ")
print(Tuple3)


# In[68]:


# Slicing of a Tuple

# Slicing of a Tuple
# with Numbers
Tuple1 = tuple('GEEKSFORGEEKS')

# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])


# In[70]:


# Deleting a Tuple

Tuple1 = (0, 1, 2, 3, 4)
del Tuple1

print(Tuple1)


# In[71]:


# Python program to demonstrate
# Creation of Set in Python

# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)

# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)


# In[72]:


# Creating a Set with
# a List of Numbers
# (Having duplicate values)
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)

# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)


# In[73]:


# Another Method to create sets in Python3

# Set containing numbers
my_set = {1, 2, 3}

print(my_set)

# This code is contributed by sarajadhav12052009


# In[74]:


# Python program to demonstrate
# Addition of elements in a Set

# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6, 7))
print("\nSet after Addition of Three elements: ")
print(set1)

# Adding elements to the Set
# using Iterator
for i in range(1, 6):
	set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)


# In[75]:


# Python program to demonstrate
# Addition of elements in a Set

# Addition of elements to the Set
# using Update function
set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)


# In[76]:


# Python program to demonstrate
# Accessing of elements in a set

# Creating a set
set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set1)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
	print(i, end=" ")

# Checking the element
# using in keyword
print("Geeks" in set1)


# In[77]:


# Python program to demonstrate
# Deletion of elements in a Set

# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,
			7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing elements from Set
# using Remove() method
set1.remove(5)
set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)

# Removing elements from Set
# using Discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after Discarding two elements: ")
print(set1)

# Removing elements from Set
# using iterator method
for i in range(1, 5):
	set1.remove(i)
print("\nSet after Removing a range of elements: ")
print(set1)


# In[78]:


# Python program to demonstrate
# Deletion of elements in a Set

# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,
			7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing element from the
# Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)


# In[79]:


#Creating a set
set1 = set([1,2,3,4,5])
print("\n Initial set: ")
print(set1)


# Removing all the elements from
# Set using clear() method
set1.clear()
print("\nSet after clearing all the elements: ")
print(set1)


# In[80]:


# Python program to demonstrate
# working of a FrozenSet

# Creating a Set
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')

Fset1 = frozenset(String)
print("The FrozenSet is: ")
print(Fset1)

# To print Empty Frozen Set
# No parameter is passed
print("\nEmpty FrozenSet: ")
print(frozenset())


# In[81]:


# Typecasting Objects in Python3 into sets

# Typecasting list into set
my_list = [1, 2, 3, 3, 4, 5, 5, 6, 2]
my_set = set(my_list)
print("my_list as a set: ", my_set)

# Typecasting string into set
my_str = "GeeksforGeeks"
my_set1 = set(my_str)
print("my_str as a set: ", my_set1)

# Typecasting dictionary into set
my_dict = {1: "One", 2: "Two", 3: "Three"}
my_set2 = set(my_dict)
print("my_dict as a set: ", my_set2)

# This code is contributed by sarajadhav12052009


# In[82]:


def create_set():
	my_set = {1, 2, 3, 4, 5}
	print(my_set)

def add_element():
	my_set = {1, 2, 3, 4, 5}
	my_set.add(6)
	print(my_set)

def remove_element():
	my_set = {1, 2, 3, 4, 5}
	my_set.remove(3)
	print(my_set)

def clear_set():
	my_set = {1, 2, 3, 4, 5}
	my_set.clear()
	print(my_set)

def set_union():
	set1 = {1, 2, 3}
	set2 = {4, 5, 6}
	my_set = set1.union(set2)
	print(my_set)

def set_intersection():
	set1 = {1, 2, 3, 4, 5}
	set2 = {4, 5, 6, 7, 8}
	my_set = set1.intersection(set2)
	print(my_set)

def set_difference():
	set1 = {1, 2, 3, 4, 5}
	set2 = {4, 5, 6, 7, 8}
	my_set = set1.difference(set2)
	print(my_set)

def set_symmetric_difference():
	set1 = {1, 2, 3, 4, 5}
	set2 = {4, 5, 6, 7, 8}
	my_set = set1.symmetric_difference(set2)
	print(my_set)

def set_subset():
	set1 = {1, 2, 3, 4, 5}
	set2 = {2, 3, 4}
	subset = set2.issubset(set1)
	print(subset)

def set_superset():
	set1 = {1, 2, 3, 4, 5}
	set2 = {2, 3, 4}
	superset = set1.issuperset(set2)
	print(superset)

if __name__ == '__main__':
	create_set()
	add_element()
	remove_element()
	clear_set()
	set_union()
	set_intersection()
	set_difference()
	set_symmetric_difference()
	set_subset()
	set_superset()


# # Dictionary

# In[83]:


# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)


# In[84]:


# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)


# In[85]:


# Creating a Nested Dictionary
# as shown in the below image
Dict = {1: 'Geeks', 2: 'For',
		3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(Dict)


# In[86]:


# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)


# In[87]:


# Python program to demonstrate
# accessing a element from a Dictionary

# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])

# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])


# In[88]:


# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))


# In[89]:


# Creating a Dictionary
Dict = {'Dict1': {1: 'Geeks'},
		'Dict2': {'Name': 'For'}}

# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])


# In[90]:


# Python program to demonstrate
# Deleting Elements using del Keyword

# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Dictionary =")
print(Dict)
#Deleting some of the Dictionar data
del(Dict[1])
print("Data after deletion Dictionary=")
print(Dict)


# In[91]:


# demo for all dictionary methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy() method
dict2 = dict1.copy()
print(dict2)

# clear() method
dict1.clear()
print(dict1)

# get() method
print(dict2.get(1))

# items() method
print(dict2.items())

# keys() method
print(dict2.keys())

# pop() method
dict2.pop(4)
print(dict2)

# popitem() method
dict2.popitem()
print(dict2)

# update() method
dict2.update({3: "Scala"})
print(dict2)

# values() method
print(dict2.values())


# # Array in python

# In[92]:


# Python program to demonstrate
# Creation of Array

# importing "array" for array creations
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
	print(a[i], end=" ")
print()

# creating an array with double type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print("\nThe new created array is : ", end=" ")
for i in range(0, 3):
	print(b[i], end=" ")


# In[93]:


# Python program to demonstrate
# Adding Elements to a Array

# importing "array" for array creations
import array as arr

# array with int type
a = arr.array('i', [1, 2, 3])


print("Array before insertion : ", end=" ")
for i in range(0, 3):
	print(a[i], end=" ")
print()

# inserting array using
# insert() function
a.insert(1, 4)

print("Array after insertion : ", end=" ")
for i in (a):
	print(i, end=" ")
print()

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

print("Array before insertion : ", end=" ")
for i in range(0, 3):
	print(b[i], end=" ")
print()

# adding an element using append()
b.append(4.4)

print("Array after insertion : ", end=" ")
for i in (b):
	print(i, end=" ")
print()


# In[94]:


# Python program to demonstrate
# accessing of element from list

# importing array module
import array as arr

# array with int type
a = arr.array('i', [1, 2, 3, 4, 5, 6])

# accessing element of array
print("Access element is: ", a[0])

# accessing element of array
print("Access element is: ", a[3])

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# accessing element of array
print("Access element is: ", b[1])

# accessing element of array
print("Access element is: ", b[2])


# In[95]:


# Python program to demonstrate
# Removal of elements in a Array

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 5])

# printing original array
print("The new created array is : ", end="")
for i in range(0, 5):
	print(arr[i], end=" ")

print("\r")

# using pop() to remove element at 2nd position
print("The popped element is : ", end="")
print(arr.pop(2))

# printing array after popping
print("The array after popping is : ", end="")
for i in range(0, 4):
	print(arr[i], end=" ")

print("\r")

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print("The array after removing is : ", end="")
for i in range(0, 3):
	print(arr[i], end=" ")


# In[96]:


# Python program to demonstrate
# slicing of elements in a Array

# importing array module
import array as arr

# creating a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
	print(i, end=" ")

# Print elements of a range
# using Slice operation
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)

# Print elements from a
# pre-defined point to end
Sliced_array = a[5:]
print("\nElements sliced from 5th "
	"element till the end: ")
print(Sliced_array)

# Printing elements from
# beginning till end
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)


# In[97]:


# Python code to demonstrate
# searching an element in array


# importing array module
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print("The new created array is : ", end="")
for i in range(0, 6):
	print(arr[i], end=" ")

print("\r")

# using index() to print index of 1st occurrence of 2
print("The index of 1st occurrence of 2 is : ", end="")
print(arr.index(2))

# using index() to print index of 1st occurrence of 1
print("The index of 1st occurrence of 1 is : ", end="")
print(arr.index(1))


# In[98]:


# Python code to demonstrate
# how to update an element in array

# importing array module
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print("Array before updation : ", end="")
for i in range(0, 6):
	print(arr[i], end=" ")

print("\r")

# updating a element in a array
arr[2] = 6
print("Array after updation : ", end="")
for i in range(0, 6):
	print(arr[i], end=" ")
print()

# updating a element in a array
arr[4] = 8
print("Array after updation : ", end="")
for i in range(0, 6):
	print(arr[i], end=" ")


# In[99]:


import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 2, 5, 2])

# Count the number of occurrences of the element 2 in the array
count = my_array.count(2)

# Print the result
print("Number of occurrences of 2:", count)


# In[100]:


import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Print the original array
print("Original array:", *my_array)

# Reverse the array in place
my_array.reverse()

# Print the reversed array
print("Reversed array:", *my_array)


# In[101]:


#Python program to demonstrate

# Adding Elements to a Array

# importing "array" for array creations

import array as arr

# array with int type

a = arr.array('i', [1, 2, 3,4,5])

#printing original array

print("The before array extend : ", end =" ")

for i in range (0, 5):

	print (a[i], end =" ")
	
print()

#creating an array with using extend method

a.extend([6,7,8,9,10])

#printing original array

print("\nThe array after extend :",end=" ")

for i in range(0,10):

	print(a[i],end=" ")
	
print()


# In[102]:


#Python program to demonstrate

# Creation of Array

# importing "array" for array creations

import array as arr

#creating an array with integer type

a=arr.array('i',[1,2,3,4,5,6])

# printing original array

print("The Before extend array is :",end=" ")

for i in range(0,6):

	print(a[i],end=" ")
	
print()

# creating an array with using extend method

a.extend([7,8,9,10,11,12])

# printing original array

print("\nThe After extend array is :",end=" ")

for i in range(0,12):

	print(a[i],end=" ")

print()

#array with float type

b = arr.array('d', [2.1,2.2,2.3,2.4,2.5,2.6])

print("\nThe before extend array is :",end=" ")

for i in range(0,6):

print(b[i],end=" ")

print()

#extend function using pass the elements

b.extend([2.6,2.7,2.8,2.9])

print("\nThe after extend array is :",end=" ")

for i in range(0,9+1):

print(b[i],end=" ")

print()


# In[1]:


# Python code to illustrate
# chaining comparison operators
x = 5
print(1 < x < 10)
print(10 < x < 20 )
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)


# In[7]:


# Python code to illustrate
# chaining comparison operators
a, b, c, d, e, f = 0, 5, 12, 0, 15, 15
exp1 = a <= b < c > d is not e is f
exp2 = a is d > f is not c
print(exp1)
print(exp2)


# In[9]:


x=5
y=10
z=15

if x < y or y < z and z < x:
    print("This will not be printed as expected!")
a=x < y or y < z and z < x
print(a)


# In[12]:


x=5
y=10
z=15


if (x < y or y < z) and z < x:
    print("This will be printed as expected")
a=(x < y or y < z) and z < x
print(a)


# In[4]:


# python code to demonstrate working of zip()

# initializing list
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

# using zip() to combine two containers
# and print values
for q, a in zip(questions, answers):
    print(f"What is your {q}? I am {a}.")


# In[5]:


# python code to demonstrate working of zip()

# initializing list
questions = ['name', 'colour']
answers = ['apple', 'red', 'a circle']

# using zip() to combine two containers
# and print values
for q, a in zip(questions, answers):
    print(f"What is your {q}? I am {a}.")


# In[8]:


def add(num1, num2):
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")


# In[9]:


# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
	"""Function to check if the number is even or odd"""
	
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
print(evenOdd.__doc__)


# In[13]:


def myFun(arg1, *argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# In[14]:


def myFun(arg1, *argv):
	print("First argument :", arg1)
	print("Next argument through *argv :", *argv)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# In[4]:


class person:
    name="harry"
    occupation="software developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=person()
a.info()


# In[5]:


class person:
    name="harry"
    occupation="software developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=person()
a.name="Abhi"
a.occupation="Engineer"
a.info()


# In[14]:


def greet(fx):
    def mfx(*args,**kwargs):
        print("WELCOME TO VEER KIRANA STORE")
        fx(*args,**kwargs)
        print("THANKS FOR PURCHASING FROM VEER KIRANA STORE")
    return mfx
@greet
def hello():
    print("Hello world")
hello()
@greet
def adding(a,b):
    print(a+b)

adding(3,4)


# In[16]:


# Getters and Setters
class myclass:
    def __init__(self,value):
        self.value=value
    def show(self):
        print(f"Value  is {self._value}")
    @property
    def value(self):
        return 10*self._value
    
obj= myclass(10)
print(obj._value)
obj.show()


# In[17]:


# inheritance in python
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showdetails(self):
        print(f"The name of employee : {self.id} is {self.name}")

e1=Employee("ROHAN",300)
e1.showdetails()
e2=Employee("ROH",800)
e2.showdetails()


# In[21]:


class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showdetails(self):
        print(f"The name of employee : {self.id} is {self.name}")
class Programmer(Employee):
    def showlanguages(self):
        print("The default language is python")
        

e1=Employee("ROHAN",300)
e1.showdetails()
e2=Employee("ROH",800)
e2.showdetails()
#  please make a note from here 
#  we can take it as an example of father and a son like here class employee is a father whereas class programmer made from  employee is a children
# alright !!!! now children will contain all the properties of his father alongwith his new properties
# below is an example to understand the situation here
e3=Programmer("RAM",345)
e3.showdetails()
e3.showlanguages()


# In[27]:


# lecture number 62
#  Access modifier in Python
# There is not any thing in python like public private and protected
#  lets take a breif of this 

# PUBLIC ACCESS MODIFIER
class Employee:
    def __init__(self):
        self.name="Gemmy"
        
a=Employee()
print(a.name)


# In[28]:


# NAME MANGLING IN PYTHON
#  PRIVATE ACCESS MODIFIER
class Employee:
    def __init__(self):
        self.__name="Gemmy"
        
a=Employee()
# print(a.__name)  # ? it will raise an error
print(a._Employee__name)  # indirectly we can access 

print(a.__dir__())


# In[32]:


# PROTECTED ACCESS MODIFIER
class student:
    def __init__(self):
        self.name="Gemmy"
    
    def _funName(Self):
        return "GemmyDidi"

class subject(student):
    pass
obj= student()
print(dir(obj))  # similar to print(obj.__dir__())
obj1= subject()
print(obj.name)
print(obj._funName())
print(obj1.name)
print(obj1._funName())


# In[ ]:


# static method in python
class Math:
    def __init__(self):
        self.num=num
    
    def addtonum(self,n)

