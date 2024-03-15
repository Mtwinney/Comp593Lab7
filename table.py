import sqlite3
# Open a connection to the database.
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