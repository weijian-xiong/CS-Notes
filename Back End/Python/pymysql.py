#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","test" )

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
create_table = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT )"""
insert_value = "INSERT INTO EMPLOYEE(FIRST_NAME, \
   LAST_NAME, AGE, SEX, INCOME) \
   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
   ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # Execute the SQL command
   cursor.execute(create_table)
   cursor.execute(insert_value)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
