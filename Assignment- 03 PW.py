#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.

# A1. def keyword is used to create a function, syntax for creating a function using def keyword is as shown below:-
#     def func_name(func_arguments):
#         func_body

def odd_list():
    l1=[]
    for i in range(1,26):
        if i%2==0:
            continue
        else:
            l1.append(i)
    return l1

odd_list()


# In[30]:


# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
# to demonstrate their use.

# A2. *args is used to take multiple inputs at the same time as a tuple while
#     **kwargs are used to take multiple inputs at the same time as a dictonary
    
# Function for *args

def average(*args):
    sum=0
    for i in args:
        sum=sum+i
    print("Average is: ",sum/ len(args))
average(5,6,7,1)

# Function for **kwargs

def name(**kwargs):
    print(kwargs["fname"],kwargs["mname"],kwargs["lname"])
    
name(fname="James",mname="Buchanan",lname="Barnes")


# In[31]:


# Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
#     used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
#     16, 18, 20].

# A3. In Python, an iterator is an object used to iterate across iterable objects such as lists, tuples, dicts, and sets.
#     The iter () method is used to initialize the iterator object. Iteration is accomplished through the usage of the 
#     next () method.

l=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
count=0
for i in l:
    if count<5:
        print(i)
        count+=1


# In[32]:


# Q4.  What is a generator function in python? Why yield keyword is used? Give an example of a generator 
# function.
# A4. A generator function in Python is a special type of function that returns a generator iterator, 
#     which can be used to iterate over a sequence of elements. A generator function is defined like a normal function,
#     but instead of using the return statement to return a value, it uses the yield statement. 
#     The yield statement is used to produce a value, and the generator function can be resumed from where it left
#     off the next time next() is called on the generator.

# Here's an example of a generator function that generates the Fibonacci sequence:


#the fibonacci series program using generator yield
def fibonacci():
    """This function will generate fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i in range(10):
    print(next(fib))


# In[42]:


# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the 
# first 20 prime numbers

# A5.

def is_prime(n):
    """Function to check whether a number is sprime or not"""
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        return True
    else:
        return False

def primes():
    for i in range(1,1000):
        if(is_prime(i)):
            yield i
            
# Using next to find first 20 prime numbers
x=primes()
for i in range(20):
    print(next(x))


# In[35]:


# Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.
# A6. 

a,b = 0, 1
count = 0
while count < 10:
       print(a)
       a,b=b,a+b
       count=count+1


# In[36]:


# Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.

# Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']
    
# A7.
List = [character for character in 'pwskills']
 
# Displaying list
print(List)


# In[38]:


# Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

# A8. 

num=int(input("Enter a number for checking whether the number is palindrome or not ? "))
d=0
n=num
while(n!=0):
    r=n%10
    d= d*10 + r
    n=n//10
    
print(d)
if(num==d):
    print("Palindrome")
else:
    print("Not")


# In[39]:


# Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
# Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter
# out odd numbers.

# A9. 

def odd_numbers(n):
    return [x for x in range(0, n+1) if x%2 != 0]

odd_numbers(100)

