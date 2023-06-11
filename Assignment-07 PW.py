#!/usr/bin/env python
# coding: utf-8

# # OOP'S ASSIGNMENT 2

# In[ ]:


Q1. What is Abstraction in OOps? Explain with an example.

A5. In Object Oriented Programming, Inheritance, Polymorphism and Encapsulation go hand in hand.
    But Abstraction is also an essential element of OOP.

    For example, people do not think of a car as a set of thousands of individual parts.
    Instead they see it as a well-defined object with its own unique behavior.
    This abstraction allows people to use a car to drive without knowing the complexity of the parts that form the car.
    They can ignore the details of how the engine transmission, and braking systems work.
    Instead, they are free to utilize the object as a whole.


# In[1]:


import abc
class pwskills:
    
    @abc.abstractmethod
    def student_details(self):
        pass
    
    @abc.abstractmethod
    def student_assignments(self):
        pass
    
    @abc.abstractmethod
    def student_marks(self):
        pass


# In[5]:


class dsm(pwskills):
    
    def student_details(self):
        return "This is a method for taking student details for dsm"
    
    def student_assignments(self):
        return "This is a method for taking student assignments for dsm"


# In[6]:


dobj = dsm()
dobj.student_details()


# In[ ]:


Q2. Differentiate between Abstraction and Encapsulation. Explain with an example.

A2. Abstraction and encapsulation are complementary concepts:
    abstraction focuses on the observable behavior of an object... 
    encapsulation focuses upon the implementation that gives rise to this behavior...
    encapsulation is most often achieved through information hiding, 
    which is the process of hiding all of the secrets of object that do not contribute to its essential characteristics.


# In[7]:


#  Example to show abstraction is same as in question 1 above 
#  Example to show Encapsulation

class car:
    def __init__(self, year, make, model, speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = speed
c=car(2023,"toyata","innova",12)
# c.
# here i'm not getting any hint by presssing tab after c. This is what i have achieve using encapsulation 


# In[8]:


c.year


# In[10]:


c.__year


# In[ ]:


PLEASE NOTE HERE IN THE ABOVE LINES OF CODE that i cannot directly access the encapsulated data


# In[11]:


c._car__year


# In[ ]:


get_ipython().run_line_magic('pinfo', 'used')

A3. The main goal of the abstract base class is to provide a standardized way to test whether an object
    adheres to a given specification. It can also prevent any attempt to instantiate a subclass that 
    doesn’t override a particular method in the superclass. And finally, using an abstract class, 
    a class can derive identity from another class without any object inheritance.


# In[12]:


import abc
  
  
class AbstractClass(metaclass=abc.ABCMeta):
    def abstractfunc(self):
        return None
  
  
print(AbstractClass.register(dict))


# In[ ]:


Here, dict identifies itself as a subclass of AbstractClass.


# In[13]:


import abc
  
  
class AbstractClass(metaclass=abc.ABCMeta):
    def abstractfunc(self):
        return None
  
  
AbstractClass.register(dict)
print(issubclass(dict, AbstractClass))


# In[ ]:


get_ipython().run_line_magic('pinfo', 'abstraction')
A4. Data Abstraction in Python can be achieved through creating abstract classes and inheriting them later.
    Example:- IN Question 1 Above


# In[ ]:


Q5. Can we create an instance of an abstract class? Explain your answer
A5. Cannot be created
    An instance of an abstract class can not be created. Constructors are allowed. 
    We can have an abstract class without any abstract method.


# # THANKYOU
