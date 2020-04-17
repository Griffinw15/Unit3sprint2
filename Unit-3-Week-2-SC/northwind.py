#What are the ten most expensive items(per unit price)in the database?
#What is the avg age of an employee at the time of their hiring?(lot of arithmetic works with dates)

import sqlite3
from psycopg2.extras import execute_values

DB_FILEPATH = "UNIT-3-WEEK-2-SC/northwind_small.sqlite3"

connection = sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()

cursor.execute("SELECT * FROM OrderDetail ORDER BY UnitPrice LIMIT 10;")

cursor.execute("SELECT AVG(2020 - YEAR) FROM (SELECT EXTRACT(YEAR FROM BirthDate) FROM Employee WHERE HireDate == date);")

#What are the ten most expensive items (per unit price) in the database *and*their suppliers?
#What is the largest category (by number of unique products in it)?

#cursor.execute("SELECT * FROM OrderDetail O JOIN Product P ON O.ProductID = P.ProductID ORDER BY UnitPrice LIMIT 10;")
#couldnt figure this one out in time

cursor.execute("SELECT COUNT(distinct CategoryID) ORDER BY CategoryID FROM Category LIMIT 1;")

all_results = cursor.fetchall()
print(all_results)
​
connection.commit()
