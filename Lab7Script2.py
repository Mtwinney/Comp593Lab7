import sqlite3
import pandas as pd

# Create an SQLite database connection
conn = sqlite3.connect('social_network.db')
cur = conn.cursor()

# Define SQL query to select people aged 50 and older
select_old_people_query = """
SELECT name, age
FROM people
WHERE age >= 50
"""

# Execute SQL query to select people aged 50 and older
cur.execute(select_old_people_query)

# Fetch all query results
old_people = cur.fetchall()

# Close database connection
conn.close()

# Print name and age of old people and save to CSV file
if old_people:
    print("Old People:")
    for person in old_people:
        print(f"{person[0]} is {person[1]} years old.")

    # Convert query results to a DataFrame
    df = pd.DataFrame(old_people, columns=['Name', 'Age'])

    # Save DataFrame to CSV file
    df.to_csv('old_people.csv', index=False)
    print("Old people data saved to 'old_people.csv' file.")
else:
    print("No old people found in the database.")
