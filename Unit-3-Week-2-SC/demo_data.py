import sqlite3
from psycopg2.extras import execute_values

DB_FILEPATH = "UNIT-3-WEEK-2-SC/demo_data.sqlite3"

connection = sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()
​
create_query = "CREATE TABLE demo (
    s VARCHAR NOT NULL,
    x INT,
    y INT
);"
execute_values(cursor, create_query, rows_to_insert)
​

rows_to_insert = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
] 
​
insertion_query = "INSERT INTO test_table (name, data, data) VALUES %s"
execute_values(cursor, insertion_query, rows_to_insert)
​
#- Count how many rows you have - it should be 3!
#- How many rows are there where both `x` and `y` are at least 5?
#- How many unique values of `y` are there?

cursor.execute("SELECT COUNT(s) from demo;")

cursor.execute("SELECT COUNT(rows) from demo WHERE x>=5 AND y>=5;")

cursor.execute("SELECT COUNT(distinct y) from demo;")

all_results = cursor.fetchall()
print(all_results)
​
connection.commit()