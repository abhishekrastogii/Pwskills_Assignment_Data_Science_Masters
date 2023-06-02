#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1. Create a python program to sort the given list of tuples based on integer value using a 
# lambda function. 


# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# A4.

s = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
print("Original list of tuples:")
print(s)
s.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(s)


# In[5]:


# Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using 
# lambda and map functions.


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# A2. 

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(map(lambda x: x**2,l))
print(new_list)


# In[6]:


# Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and 
#     lambda functions


# Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    
# A3.
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new= map(lambda x: str(x),l)
print(tuple(new))


# In[9]:


# Q4.  Write a python program using reduce function to compute the product of a list containing numbers 
# from 1 to 25

# A4.
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
from functools import reduce
pro = int(reduce(lambda x,y : x*y,l))
print(pro)


# In[11]:


# Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the 
# filter function.


# [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

# A5.

l= [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
def filter_list(x):
    if x%2==0 or x%3==0:
        return x
new_list = list(filter(filter_list , l))
print(new_list)


# In[12]:


# Q6. Write a python program to find palindromes in the given list of strings using lambda and filter 
# function.


# ['python', 'php', 'aba', 'radar', 'level']

# A6.
l=['python', 'php', 'aba', 'radar', 'level']
new_list = list(filter(lambda x : x==x[::-1] ,l))
print(new_list)

