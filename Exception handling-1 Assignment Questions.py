#!/usr/bin/env python
# coding: utf-8

# Exception handling-1
# Assignment Questions

# In[ ]:


Q1. what is an exception in python ? Write the difference between exceptions and syntax errors.

A1. An Exception in Python is raised when some internal events occur which change the normal flow of the program.
    The difference between Exceptions and syntax errors is that:
       1 Syntax errors are problems in a program due to which the program will stop the execution.
       2 Exceptions are raised when an attempt is made to execute a statement or expression that is syntactically correct,
            but causes an error during execution.
       3 Exceptions come in different types, and the type is printed as part of the message.


# In[ ]:


Q2. What happened when an exception is not handled ? Explain with  an example.

A2. If an exception is not handled in a program, the program terminates abruptly and the code past the line that caused
    the exception will not get executed. To handle exceptions, you can use a try-catch block or throw them using the 
    throws keyword. If no exception handler for a given exception is present, the program stops executing with an error 
    message. If an exception is not caught, the runtime system will abort the program and an exception error will crash
    the program.


# In[ ]:


Q3. Which python statement are used to catch and handle exception explain with an example ?

A3. Try and except statements are used to catch and handle exceptions in Python. The statements that can raise exceptions 
    are kept inside the try clause and the statements that handle the exception are written inside except clause.
    Other statements used to handle exceptions in Python include:
        try/finally: Whether exception occurs or not, it automatically performs the clean-up action.
        assert: triggers an exception conditionally in the code.
        raise: manually triggers an exception in the code.
        with/as: implement context managers in older versions of Python such as - Python 2.6 & Python 3.0.


# In[ ]:


Q4. Explain with an example:
    a. try and else 
    b. finally
    c. raise
    
A4. Try: This block will test the excepted error to occur
    Else: If there is no exception then this block will be executed
    Finally: Finally block always gets executed either exception is generated or not

        try:
               # Some Code.... 

        except:
               # optional block
               # Handling of exception (if required)

        else:
               # execute if no exception

        finally:
              # Some code .....(always executed)


# In[3]:


# Example to illustrate try, else and finally
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally: 
        # this block is always executed  
        # regardless of exception generation. 
        print('This is always executed')  
 
# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)


# In[7]:


# c. raise :
#     To chain exceptions, use the raise from statement instead of a simple raise statement.
#     This will give you information about both errors.


def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e
        
example()


# In[8]:


Both exceptions are captured in the traceback. A normal except statement is used to catch such an exception.
However, __cause__ attribute of the exception object can be looked to follow the exception chain as explained 
in the code given below.

Code #2 :

try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)
    if e.__cause__:
        print('Cause:', e.__cause__)


# In[ ]:


Q5. What are Custom Exceptions in python? Why do we need Custom Exceptions? Explain with an example.

A5. exceptions are just regular classes that inherit from the Exception class. This makes it super easy to create our
    own custom exceptions, which can make our programs easier to follow and more readable. 
    An exception need not be complicated, just inherit from Exception:


# In[9]:


class MyCustomException(Exception):
     pass
raise MyCustomException()


# In[ ]:


Having custom exceptions - tailored to your specific use cases and that you can raise and catch in specific circumstances
- can make your code much more readable and robust, and reduce the amount of code you write later to try and figure out
what exactly went wrong.

Of course, you can get as fancy as you want. You can send additional information, like messages, to your exceptions.
Just add an __init__() method to your exception class, with whatever arguments you want.


# In[10]:


#Q6. Create a custom exception class. Use this class to handle an exception.
#A6. 
class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Got an incorrect value of {value}"
        super().__init__(message)
        
my_value = 9999
if my_value > 100:
    raise IncorrectValueError(my_value)


# # THANKYOU
