#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q1. How do you comment code in Python? What are the different types of comments?
# A1. BY pressing control plus forward slash we can simply put a comment in python
#     There are two ways of commenting a code in python
#     (i)  SINGLE LINE COMMENTS->using # we can comment a single line in python
#     (ii) MULTI LINE COMMENTS-> using triple quotes """abcdefg""""


# In[1]:


# Q2. What are variables in Python? How do you declare and assign values to variables?
# A2. variables are just like the container which stores the value in themselves
#     for example a=5 --> here a is a variable which stores the value 5
#     IN PYTHON it is very simple to declare a variable than in any other programming language 
#     By simply write the variable name as any valid identifier we can declare a variable in python
#     for example->
#                 (i) a
#                 (ii)b
#             There is no need to declare the type of the variable in python

#     Assigning value to a vaiable:-
#         by simply writing the value in equal to the identifier we can initialize  a variable
#         for example->
#                     (i) a=5
#                     (ii) b="Abhishek rastogi"
#                     (iii) c=5.6


# In[2]:


# Q3. How do you convert one data type to another in Python?
# A3. By using Explicit Type Conversion we can simply convert the one data type into another one
#     for example:
#         a=5
#         here, a is an integer
#         to convert this integer value into string we can simply write like this
#         b=str(a)
#         here b is assigning the value of a as string value
#    And similarly we can convert any data type into another data type


# In[3]:


# Q4. How do you write and execute a Python script from the command line?
# A4. By opening the command prompt from the starting menu and after it press the python3 there 
#       a three greater than symbol appears on your screen like this  >>> , and from where we can write and execue our script
#       REPL-> READ EVALUATED PRINT LOOP
#         Here, in command line it works on the concept of repl
#         Although it is a fast method to execute the scripts of python , still it is not adapted for the work because it leads 
#         to the maintanability issue.


# In[7]:


# Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].
# A5. Program is as follows
 
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3])


# In[9]:


# Q6. What is a complex number in mathematics, and how is it represented in Python?
# A6. Complex numbers are the set of imaginary numbers which consists of iota(i)
#     All the numbers other than real number are complex numbers
     
#     In Python, we can represent complex number by simply writing the real part and imaginary part eith the subscript 'j'
#     for example:
#         a= 5+9j
#         here a is a type of complex number 
#         whose real part is 5
#         and imag part is 9
        
a=5+9j
print(type(a))
print(a.real)
print(a.imag)


# In[11]:


# Q7. What is the correct way to declare a variable named age and assign the value 25 to it?
# A7. By simply writing the variable name= value that is assigning to that variable
 
age=25
print(age)


# In[12]:


# Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable
# belong to?

# A8. Program to simulate the above problem

a=9.99
print(type(a))


# In[14]:


# Q9. Create a variable named name and assign your full name to it as a string. How would you print the
# value of this variable?

name="Abhishek Rastogi"
print(name)


# In[17]:


# Q10. Given the string "Hello, World!", extract the substring "World".
# A10. 
str="Hello, World!"
print(str[7:12])


# In[18]:


# Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are
# currently a student or not.
# A11.
is_student=True
print(is_student)


# # THANKYOU #
