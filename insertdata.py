import sqlite3
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