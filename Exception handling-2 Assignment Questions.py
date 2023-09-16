#!/usr/bin/env python
# coding: utf-8

# Exception handling-2
# Assignment Questions

# In[ ]:


Q1. Explain why we have to use the Exception class while creating a Custom Exception.
    Note: Here Exception class refers to the base class for all the exceptions.
Q2. Write a python program to print Python Exception Hierarchy.
Q3. What errors are defined in the ArithmeticError class? Explain any two with an example.
Q4. Why LookupError class is used? Explain with an example KeyError and IndexError.
get_ipython().run_line_magic('pinfo', 'ModuleNotFoundError')
Q6. List down some best practices for exception handling in python.


# In[ ]:


Q1. Explain why we have to use the Exception class while creating a Custom Exception.

A1. We use the Exception class while creating a Custom Exception in Python for the following reasons:
       1 To improve readability of your code.
       2 To enhance reusability of features.
       3 To provide custom messages/instructions to users for specific use cases.
       4 To add functionality to the custom exception classes like adding attributes and properties, adding methods,
            overriding the str and repr methods, and doing anything else that you can do with regular classes.


# In[ ]:


Q2. Write a python program to print Python Exception Hierarchy.

A2. For printing the tree hierarchy we will use inspect module in Python. The inspect module provides useful functions 
    to get information about objects such as modules, classes, methods, functions,  and code objects.
    For example, it can help you examine the contents of a class, extract and format the argument list for a function.
    
    For building a tree hierarchy we will use inspect.getclasstree().


# In[1]:


# import inspect module
import inspect

# our treeClass function
def treeClass(cls, ind = 0):

    # print name of the class
    print ('-' * ind, cls.__name__)

    # iterating through subclasses
    for i in cls.__subclasses__():
        treeClass(i, ind + 3)

print("Hierarchy for Built-in exceptions is : ")

# inspect.getmro() Return a tuple
# of class cls’s base classes.

# building a tree hierarchy
inspect.getclasstree(inspect.getmro(BaseException))

# function call
treeClass(BaseException)


# In[ ]:


Q3. What errors are defined in the ArithmeticError class? Explain any two with an example.

A3. ArithmeticError is a class of errors that occur while performing mathematical operations. Some of the errors defined
    in the ArithmeticError class are:
        
        ZeroDivisionError: This error is raised when a number is divided by zero. For example, 5/0 will raise a 
            ZeroDivisionError.
            
        OverflowError: This error is raised when the result of an arithmetic operation is too large to be 
            represented. For example, 2**1000 will raise an OverflowError.


# In[ ]:


Q4. Why LookupError class is used? Explain with an example KeyError and IndexError.
A4. The LookupError exception in Python is used as the base class for all exceptions that are raised when an index or 
    a key is not found for a sequence or dictionary respectively. You can use LookupError exception class to handle 
    both IndexError and KeyError exception classes. An IndexError is raised when a sequence reference is out of range,
    while a KeyError is raised when a dictionary key is not found.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'ModuleNotFoundError')

A5. ImportError is raised when an import statement has trouble successfully importing the specified module.
    It can usually be eliminated by adding a file named init.py to the directory and then adding this directory 
    to $PYTHONPATH1.
    
    ModuleNotFoundError is a subclass of ImportError that is raised when the interpreter cannot find the specified 
    module. This can happen if the module is misspelled, not installed, or not in the correct location. The error 
    message shows the name of the module that Python cannot locate.


# In[ ]:


Q6. List down some best practices for exception handling in python.
A6. Python Exception Handling Best Practices

1. Use Exceptions for Exceptional Cases Exceptions are, by definition, exceptional. ...
2. Don’t Swallow the Exception When you “swallow” an exception, you essentially ignore it. ...
3. Catch Specific Exceptions ...
4. Always Clean Up Resources in a Finally Block ...
5. Avoid Raising Generic Exceptions ...
6. Raise Custom Exceptions ...
7. Define Your Own Exception Hierarchy ...


# # THANKYOU
