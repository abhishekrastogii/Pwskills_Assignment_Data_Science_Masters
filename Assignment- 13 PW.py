#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use 
get_ipython().run_line_magic('pinfo', 'databases')

Q2. State and Explain the features of MongoDB.

Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.

Q4. Using the database and the collection created in question number 3, write a code to insert one record, 
and insert many records. Use the find() and find_one() methods to print the inserted record.

Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to 
demonstrate this.

Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.

Q7. Explain why delete_one(), delete_many(), and drop() is used


# In[ ]:


Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use 
get_ipython().run_line_magic('pinfo', 'databases')


# In[ ]:


A1. MongoDB is an open-source document database built on a horizontal scale-out architecture that uses a flexible schema
    for storing data. Founded in 2007, MongoDB has a worldwide following in the developer community.

    Instead of storing data in tables of rows or columns like SQL databases, each record in a MongoDB database is a 
    document described in BSON, a binary representation of the data. Applications can then retrieve this information
    in a JSON format.
    
    Most databases can be categorized as either relational or non-relational. Non-relational databases are sometimes 
    referred to as “NoSQL,” which stands for Not Only SQL. The main difference between these is how they store their
    information.

    A non-relational database stores data in a non-tabular form, and tends to be more flexible than the traditional,
    SQL-based, relational database structures. It does not follow the relational model provided by traditional 
    relational database management systems.


# In[ ]:


Q2. State and Explain the features of MongoDB.


# In[ ]:


A2. MongoDB is a scalable, flexible NoSQL document database platform designed to overcome the relational databases approach 
    and the limitations of other NoSQL solutions. MongoDB is well known for its horizontal scaling and load balancing
    capabilities,which has given application developers an unprecedented level of flexibility and scalability.

    MongoDB Atlas is the leading global cloud database service for modern applications. Using Atlas, developers can deploy
    fully managed cloud databases across AWS, Azure, and Google Cloud. Best-in-class data security and privacy standards 
    practices mean that developers can rest easy knowing that they have instant access to the availability, scalability,
    and compliance they require for enterprise-level application development.

    The MongoDB database platform has been downloaded over 200 million times with over 1.8 million MongoDB University
    registrations. There are drivers for 10+ languages, with dozens more added by the community. Best of all,
    MongoDB is completely free to use.

    MongoDB provides developers with a number of useful out-of-the-box capabilities, whether you need to run privately
    on site or in the public cloud.


# In[ ]:


Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.


# In[ ]:


A3.


# In[4]:


pip install pymongo


# In[5]:


import pymongo
client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.kfojhtx.mongodb.net/?retryWrites=true&w=majority")
db = client.test


# In[6]:


db


# In[7]:


client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.kfojhtx.mongodb.net/?retryWrites=true&w=majority")


# In[8]:


db = client['pwskill']


# In[ ]:


Q4. Using the database and the collection created in question number 3, write a code to insert one record, 
and insert many records. Use the find() and find_one() methods to print the inserted record.


# In[ ]:


A4.


# In[9]:


data = { "name":"sudh", "class":"dsm","time":"flexi"}


# In[10]:


coll_pwskills = db["my_record"]


# In[11]:


coll_pwskills.insert_one(data)


# In[12]:


data1 = {"mail_id":"Abhi@gmail",
        "phone_number":34222322223,
        "Address":"mawana"}


# In[13]:


coll_pwskills.insert_one(data1)


# In[14]:


data2 = [
     { "name":"sudh", "class":"dsm","time":"flexi"},
     {"mail_id":"Abhi@gmail","phone_number":34222322223,"Address":"mawana"},
     { "name":"abhi", "class":"dm","time":"exi"}
]


# In[15]:


coll_pwskills.insert_many(data2)


# In[ ]:


Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to 
demonstrate this.


# In[ ]:


A5.


# In[16]:


for i in coll_pwskills.find():
    print(i)


# In[ ]:


Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.


# In[ ]:


A6. The sort() method specifies the order in which the query returns the matching documents from the given collection.


# In[20]:


# db.coll_pwskills.sort({data1:1 or -1})


# In[ ]:


Q7. Explain why delete_one(), delete_many(), and drop() is used


# In[ ]:


A7. 


# In[23]:


coll_pwskills.delete_one(data1)


# In[25]:


coll_pwskills.delete_many(data1)


# In[26]:


data1


# In[ ]:


db.collection_name.drop_indexes()

