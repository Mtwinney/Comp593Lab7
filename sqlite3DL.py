import sqlite3
# Opens a connection to an SQLite database.
# Returns a Connection object that represent the database connection.
# A new database file will be created if it doesn't already exist.
con = sqlite3.connect('social_network.db')
# Get a Cursor object that can be used to run SQL queries on the database.
cur = con.cursor()
# Define an SQL query that creates a table named 'people'.
# Each row in this table will hold information about a specific person.
create_ppl_tbl_query = """
CREATE TABLE IF NOT EXISTS people
(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL,
address TEXT NOT NULL,
city TEXT NOT NULL,
province TEXT NOT NULL,
bio TEXT,
age INTEGER,
created_at DATETIME NOT NULL,
updated_at DATETIME NOT NULL
);
"""
# Execute the SQL query to create the 'people' table.
# Database operations like this are called transactions.
cur.execute(create_ppl_tbl_query)
# Commit (save) pending transactions to the database.
# Transactions must be committed to be persistent.
con.commit()
# Close the database connection.
# Pending transactions are not implicitly committed, so any
# pending transactions that have not been committed will be lost.
con.close()

from datetime import datetime
con = sqlite3.connect('social_network.db')
cur = con.cursor()
# Define an SQL query that inserts a row of data in the people table.
# The ?'s are placeholders to be fill in when the query is executed.
# Specific values can be passed as a tuple into the execute() method.
add_person_query = """
INSERT INTO people
(
name,
email,
address,
city,
province,
bio,
age,
created_at,
updated_at
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""
# Define a tuple of data for the new person to insert into people table
# Data values must be in the same order as specified in query
new_person = ('Bob Loblaw',
'bob.loblaw@whatever.net',
'123 Fake St.',
'Fakesville',
'Fake Edward Island',
'Enjoys making funny sounds when talking.',
46,
datetime.now(),
datetime.now())
# Execute query to add new person to people table
cur.execute(add_person_query, new_person)
con.commit()
con.close()
