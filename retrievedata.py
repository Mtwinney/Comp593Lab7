import sqlite3
from pprint import pprint
con = sqlite3.connect('social_network.db')
cur = con.cursor()
# Query the database for all information for all people.
cur.execute('SELECT * FROM people')
# Fetch all query results.
# The fetchall() method returns a list, where each list item
# is a tuple containing data from one row in the people table.
all_people = cur.fetchall()
# Pretty print (pprint) outputs data in an easier to read format.
pprint(all_people)
con.commit()
con.close()