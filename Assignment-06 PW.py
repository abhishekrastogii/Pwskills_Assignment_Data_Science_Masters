#!/usr/bin/env python
# coding: utf-8

# # OOP'S ASSIGNMENT

# In[ ]:


Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

A1. A class is a user-defined blueprint or prototype from which objects are created.
    Classes provide a means of bundling data and functionality together. Creating a new 
    class creates a new type of object, allowing new instances of that type to be made.
    Each class instance can have attributes attached to it for maintaining its state.
    Class instances can also have methods (defined by their class) for modifying their state.


# In[ ]:


# Syntax: Class Definition

class ClassName:
    pass


# In[ ]:


# Creting an object of the above class 

obj = ClassName()
print(obj.atrr)


# In[2]:


# Example to illustrate the concept 

class pwskills:
    
    def welcome_message(self):
        print("Welcome to PWSKILLS")
        

rohan=pwskills()
rohan.welcome_message()


# In[ ]:


Q2. Name the four pillars of OOPs.

A2. The four pillars of object-oriented programming are:

    1. Abstraction 
    2. Encapsulation 
    3. Inheritance 
    4. Polymorphism


# In[ ]:


Q3. Explain why the __init__() function is used. Give a suitable example.

A3. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class
    is created. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed
    at the time of Object creation. It is run as soon as an object of a class is instantiated.
    
    The method is useful to do any initialization you want to do with your object.


# In[3]:


# A Sample class with init method

class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person('Nikhil')
p.say_hi()


# In[ ]:


get_ipython().run_line_magic('pinfo', 'OOPs')
A4. self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class
    in python. It binds the attributes with the given arguments.

    The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes.
    Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically,
    but not received automatically: the first parameter of methods is the instance the method is called on.


# In[ ]:


Q5. What is inheritance? Give an example for each type of inheritance.

A5. Inheritance allows you to inherit the properties of a class, i.e., base class to another, i.e., derived class.
    The benefits of Inheritance in Python are as follows:

    1. It represents real-world relationships well.
    
    2. It provides the reusability of a code. We don’t have to write the same code again and again.
        Also, it allows us to add more features to a class without modifying it.
        
    3. It is transitive in nature, which means that if class B inherits from another class A, then 
        all the subclasses of B would automatically inherit from class A.
        
    4. Inheritance offers a simple, understandable model structure. 
    
    5. Less development and maintenance expenses result from an inheritance. 


# In[4]:


# MULTILEVEL INHERITANCE 
class class1:
    
    def test_class1(self):
        return "This is a method from class1"

class class2(class1):
    
    def test_class2(self):
        return "This is a method from class2" 
    
class class3(class2):
    pass

obj = class3()
obj.test_class1()


# In[6]:


# MULTIPLE INHERITANCE 
class class1:
    def test_class1(self):
        return "This is class 1"
    
class class2:
    def test_class2(self):
        return "This is class 2"
    
class class3(class1, class2):
    pass

obj = class3()
obj.test_class1()


# # THANKYOU
