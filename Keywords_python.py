#!/usr/bin/env python
# coding: utf-8

# In[3]:


# here we will get the list of all keywords
import keyword
print(keyword.kwlist)
# also like this
from keyword import kwlist
print(kwlist)


# In[4]:


# true false None
print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])


# In[4]:


# and, or, not, is, in

print(True or False)
print(False and True)
print(not True)
# using "in" to check
if 's' in 'geeksforgeeks':
    print("s is part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")

# using "in" to loop through
for i in 'geeksforgeeks':
    print(i, end=" ")
print()
# using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' ' is ' ')

# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})


# In[5]:


# for, while, break, continue
# Using for loop
for i in range(10):
    print(i, end=" ")
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
        print(i, end=" ")
    i += 1


# In[6]:


# if, else , elif
i = 20
if (i == 10):
    print("i is 10")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")


# In[7]:


# def keyword
def fun():
    print("Inside Function")

fun()


# In[8]:


# Return, Yield Keyword

def fun():
    S = 0
    for i in range(10):
        S += i
    return S
print(fun())

def fun():
    S = 0
    for i in range(10):
        S += i
        yield S
for i in fun():
    print(i)


# In[13]:


# class keyword
class Dog:
    a= "mammal"
    b= "dog"
    def fun(self):
        print("I'm a", self.a)
        print("I'm a", self.b)

# Driver code
# Object instantiation
Rodger = Dog()
# Accessing class attributes
# and method through objects
print(Rodger.a)
Rodger.fun()


# In[11]:


# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')
# with open('"C:\Users\abhis\Desktop\hi\bit.txt"', 'w') as file:
#     file.write('hello world !')


# #as
# #as keyword is used to create the alias for the module imported. i.e giving a new name to the imported module. E.g import math #as mymath.

# In[20]:


# as
import math as gemmy
print(gemmy.factorial(5))


# In[21]:


# pass
n = 10
for i in range(n):
	# pass can be used as placeholder
	# when code is to added later
	pass


# Lambda
# Lambda keyword is used to make inline returning functions with no statements allowed internally. 

# In[22]:


# Lambda keyword
g = lambda x: x*x*x

print(g(7))


# In[13]:


# import,from keyword
from math import factorial
import math
print(math.factorial(10))
print(factorial(10)) #direct call to factorial as function without writing math.   -->use of from here


# In[18]:


# try, except, raise, finally, and assert Keywords
a,b=(int(i) for i in input("Enter a and b ").split())
try:
    k = a//b # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
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


# In[25]:


# del keyword
a = 20
b = "GeeksForGeeks"

# check if my_variable1 and my_variable2 exists
print(a)
print(b)

# delete both the variables
del a
del b

# check if my_variable1 and my_variable2 exists
print(a)
print(b)


# In[27]:


# global variable
a = 15
b = 10

# function to perform addition
def add():
	c = a + b
	print(c)

# calling a function
add()

# nonlocal keyword
def fun():
	var1 = 10

	def gun():
		# tell python explicitly that it
		# has to access var1 initialized
		# in fun on line 2
		# using the keyword nonlocal
		nonlocal var1
		
		var1 = var1 + 10
		print(var1)

	gun()
fun()


# In[28]:


# Assigning multiple values in single line

a,b,c="geeks","for","geeks"
print(a+b+c)


# In[29]:


# Initialising variables using Conditional Operator
a = 1 if 20 > 10 else 0
print("The value of a is: " ,a)


# In[ ]:




