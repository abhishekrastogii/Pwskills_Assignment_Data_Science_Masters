#!/usr/bin/env python
# coding: utf-8

# Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed 
# and average_of_vehicle. 
# 
# Q2.  Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class. 
# Create a method named seating_capacity which takes capacity as an argument and returns the name of 
# the vehicle and its seating capacity.
# 
# Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.
# 
# Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this 
# class.
# 
# Q5.What is method overriding in python? Write a python code to demonstrate method overriding.

# Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed and average_of_vehicle.
# A1. 

# In[17]:


class vehicle:
    
    def __init__(self,name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle
        
    def print(self):
        return self.name_of_vehicle, self.max_speed, self.average_of_vehicle
    
    def name(self):
        return self.name_of_vehicle
    
object = vehicle("Honda", 250 , 95000)
object.print()


# Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
#     Create a method named seating_capacity which takes capacity as an argument and returns the name of the vehicle
#     and its seating capacity.
# A2. 

# In[21]:


# Parent class: Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name

# Child class: Car
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def seating_capacity(self, capacity):
        return f"{self.name} has a seating capacity of {capacity} people."

# Create an instance of the Car class
car = Car("Toyota")

# Call the seating_capacity method
capacity = 5
result = car.seating_capacity(capacity)

# Print the result
print(result)


# Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.
# A3.
# 
# MULTIPLE INHERITANCE 
# 
# Multiple inheritance is a feature of some object-oriented computer programming languages in which an object or class can 
# inherit features from more than one parent object or parent class. It is distinct from single inheritance, where an 
# object or class may only inherit from one particular object or class. 

# In[27]:


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


# In[24]:


obj.test_class2()


# Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this 
#     class.
#     
# A4. In Python, getters and setters are not the same as those in other object-oriented programming languages.
#     Basically, the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation.
#     Private variables in python are not actually hidden fields like in other object oriented languages.
#     Getters and Setters in python are often used when:
# 
#     We use getters & setters to add validation logic around getting and setting a value.
#     To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

# In[28]:


class car:
    def __init__(self, year, make, model, speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = 0
    
    def set_speed(self,speed):
        self.__speed = 0 if speed < 0 else speed
    
    def get_speed(self):
        return self.__speed


# In[29]:


d=car(2023,"maruti","alto",23)


# In[30]:


d.set_speed(40)


# In[31]:


d.get_speed()


# Q5. What is method overriding in python? Write a python code to demonstrate method overriding.
# 
# A5. Method overriding is an ability of any object-oriented programming language that allows a subclass or child class
#     to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes.
#     When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a
#     method in its super-class, then the method in the subclass is said to override the method in the super-class. 

# In[33]:


# Defining parent class
class Parent():
      
    def __init__(self):
        self.value = "Inside Parent"
          
    def show(self):
        print(self.value)
          
# Defining child class
class Child(Parent):
      
    def __init__(self):
        self.value = "Inside Child"
          
    def show(self):
        print(self.value)
          
          
# Driver's code
obj1 = Parent()
obj2 = Child()
  
obj1.show()
obj2.show()


# # THANKYOU 
