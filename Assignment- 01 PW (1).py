#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Question 1:
Q1. Create one variable containing following type of data:
(i) string
(ii) list
(iii) float
(iv) tuple
"""
# Answer:
# Here this list variable contains string,list,float and tuple
list=["PW",[1,2,3],3.4,(1,2,3)]
print(list)


# In[6]:


"""Question 2:
Given are some following variables containing data:
What will be the data type of the above given variable ?
"""
var1 = ''
var2 = '[ DS , ML , Python]'
var3 = [ 'DS' , 'ML' , 'Python' ]
var4 = 1

# Answer:
"""
Without compile the code lets answer these questions
(i) string
(ii) string
(iii) list
(iv) integer
"""

# With the help of compiler

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))


# In[7]:


"""
Q3. Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) **
"""
# Answer:
a = int(input("Enter first numeric operand"))
b = int(input("Enter second numeric operand"))
div = a / b
mod = a % b
floor_div  = a // b
power = a ** b
print(div)
print(mod)
print(floor_div)
print(power)


# In[10]:


"""Question 4:
Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type.
"""
# Answer
list=[1,2,3,"Abhi","Gemmy",[2,3],(3,2),2.3,4.5,2]
for i in list:
    print(i)


# In[19]:


"""Question 5:
Verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.
"""
# Answer
A=eval(input("Enter first numeric operand"))
B=eval(input("Enter second numeric operand"))
if(A%B==0):
    a=A/B
    print(f"A is divisible by B {a} times")
else:
    print("A is not divisible by B")


# In[12]:


"""Question 6: 
Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not.
"""
# Answer
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in l:
    if(i%3==0):
        print(f"{i} is divisible by 3")
    else:
        print(f"{i} is not divisible by 3")


# In[15]:


"""Question 7:
What do you understand about mutable and immutable data types? Give examples for both showing
this property.
"""
# Answer:
# MUTABLE :- which can be change for example list
# IM MUTABLE :- which can not be change for example tuple
# Example to show mutable data types
list=[1,2,3,4,5]
list[0]=9
print(list)

# Example to show immutable data types
tuple=(1,2,3,4,5)
tuple[0]=9
print(tuple)


# # THANKYOU

# In[ ]:




