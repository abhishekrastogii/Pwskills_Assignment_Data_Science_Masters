#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. What is a database? Differentiate between SQL and NoSQL databases.

Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.

Q4. What is DQL? Explain SELECT with an example.

Q5. Explain Primary Key and Foreign Key.

Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

Q7. Give the order of execution of SQL clauses in an SQL query


# In[ ]:


Q1. What is a database? Differentiate between SQL and NoSQL databases.


# In[ ]:


A1. A database is an organized collection of structured information, or data, typically stored electronically in a
    computer system. A database is usually controlled by a database management system (DBMS). Together, the data and 
    the DBMS, along with the applications that are associated with them, are referred to as a database system, often 
    shortened to just database.
    Data within the most common types of databases in operation today is typically modeled in rows and columns in a 
    series of tables to make processing and data querying efficient. The data can then be easily accessed, managed,
    modified, updated, controlled, and organized. Most databases use structured query language (SQL) for writing and
    querying data.

    Main differences between NoSQL and SQL
    
    1. Type 
    
    SQL databases are primarily called Relational Databases (RDBMS); whereas NoSQL databases are primarily called 
    non-relational or distributed databases. 

    2. Language 
    
    SQL databases define and manipulate data-based structured query language (SQL). Seeing from a side this 
    language is extremely powerful. SQL is one of the most versatile and widely-used options available which makes
    it a safe choice, especially for great complex queries. But from another side, it can be restrictive. 
    SQL requires you to use predefined schemas to determine the structure of your data before you work with it.
    Also, all of your data must follow the same structure. This can require significant up-front preparation which
    means that a change in the structure would be both difficult and disruptive to your whole system. 
 

    A NoSQL database has a dynamic schema for unstructured data. Data is stored in many ways which means it can be
    document-oriented, column-oriented, graph-based, or organized as a key-value store. This flexibility means that
    documents can be created without having a defined structure first. Also, each document can have its own unique 
    structure. The syntax varies from database to database, and you can add fields as you go. 


# In[ ]:


Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.


# In[ ]:


A2. Data Definition Language(DDL) is a subset of SQL and a part of DBMS(Database Management System).
    DDL consist of Commands to commands like CREATE, ALTER, TRUNCATE and DROP.
    These commands are used to create or modify the tables in SQL.

    DDL Commands :  Create
                    Alter 
                    truncate
                    drop
                    Rename 
                    
    CREATE :
    This command is used to create a new table in SQL. The user has to give information like table name,
    column names, and their datatypes.

    Syntax –

    CREATE TABLE table_name
    (
    column_1 datatype,
    column_2 datatype,
    column_3 datatype,
    ....
    );
    Example –   CREATE TABLE Student_info
                (
                College_Id number(2),
                College_name varchar(30),
                Branch varchar(10)
                );
        
    Command-2 :
    ALTER :
    This command is used to add, delete or change columns in the existing table. The user needs to know 
    the existing table name and can do add, delete or modify tasks easily.

    Syntax –
    
    ALTER TABLE table_name
    ADD column_name datatype;
    
    Example –   ALTER TABLE Student_info
                ADD CGPA number;
        
    Command-3 :
    TRUNCATE :
    This command is used to remove all rows from the table, but the structure of the table still exists.

    Syntax –
    
    TRUNCATE TABLE table_name;
    
    Example –   TRUNCATE TABLE Student_info;
    
    Command-4 :
    DROP :
    This command is used to remove an existing table along with its structure from the Database.

    Syntax –

    DROP TABLE table_name;
    
    Example -   DROP TABLE Student_info;
    
    Command -5
    RENAME:
    It is possible to change name of table with or without data in it using simple RENAME command.
    We can rename any table object at any point of time.
    
    Syntax –

    RENAME TABLE <Table Name> To <New_Table_Name>;
    
    Example:     RENAME TABLE Employee To EMP;


# In[ ]:


Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.


# In[ ]:


A3. DML(Data Manipulation Language)

    The SQL commands that deal with the manipulation of data present in the database belong to DML or 
    Data Manipulation Language and this includes most of the SQL statements.
    It is the component of the SQL statement that controls access to data and to the database.
    Basically, DCL statements are grouped with DML statements.

    List of DML commands: 

    INSERT: It is used to insert data into a table.
    UPDATE: It is used to update existing data within a table.
    DELETE: It is used to delete records from a database table.
    LOCK: Table control concurrency.
    CALL: Call a PL/SQL or JAVA subprogram.
    EXPLAIN PLAN: It describes the access path to data.


# In[ ]:


Q4. What is DQL? Explain SELECT with an example.


# In[ ]:


A4. DQL (Data Query Language)
    DQL statements are used for performing queries on the data within schema objects.
    The purpose of the DQL Command is to get some schema relation based on the query passed to it.
    We can define DQL as follows it is a component of SQL statement that allows getting data from 
    the database and imposing order upon it. It includes the SELECT statement.
    This command allows getting the data out of the database to perform operations with it.
    When a SELECT is fired against a table or tables the result is compiled into a further temporary table, 
    which is displayed or perhaps received by the program i.e. a front-end.

    List of DQL: 

    SELECT: It is used to retrieve data from the database.
        
    Syntax: SELECT column1,column2 FROM table_name 
            column1 , column2: names of the fields of the table
            table_name: from where we want to apply query
                
    SELECT * FROM table_name; 

    asterisks represent all attributes of the table


# In[ ]:


Q5. Explain Primary Key and Foreign Key.


# In[ ]:


A5.  PRIMARY KEY	FOREIGN KEY

       1. A primary key is used to ensure data in the specific column is unique.
          A foreign key is a column or group of columns in a relational database table that provides a link between
          data in two tables.
            
       2. It uniquely identifies a record in the relational database table.
          It refers to the field in a table which is the primary key of another table.
        
       3. Only one primary key is allowed in a table.
          Whereas more than one foreign key is allowed in a table.
        
       4. It is a combination of UNIQUE and Not Null constraints.
          It can contain duplicate values and a table in a relational database.
        
       5. It does not allow NULL values.
          It can also contain NULL values.


# In[ ]:


Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.


# In[ ]:


A6. Connecting to the Database
    The mysql.connector provides the connect() method used to create a connection between the MySQL database and the
    Python application. The syntax is given below.

    Syntax:
    Conn_obj= mysql.connector.connect(host = <hostname>, user = <username>, passwd = <password>)  


# In[8]:


# import MySQLdb

# db = MySQLdb.connect(host="localhost",user="appuser",passwd="",db="onco")
# cursor = db.cursor()

# cursor.execute("SELECT * FROM location")

# rows = cursor.rowcount

# for x in range(rows):
#     row = cursor.fetchone()
#     print(row[0], "-->", row[1])

# db.close()


# In[ ]:


Q7. Give the order of execution of SQL clauses in an SQL query.


# In[ ]:


A7.Six Operations to Order: SELECT, FROM, WHERE, GROUP BY, HAVING, and ORDER BY

