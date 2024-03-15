"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from faker import Faker
from datetime import datetime
import random

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # Open a connection to the database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Define an SQL query to create the people table
    create_people_query = """
    CREATE TABLE IF NOT EXISTS people (
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

    # Execute the SQL query to create the people table
    cur.execute(create_people_query)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # Open a connection to the database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Create a faker object for English Canadian locale
    fake = Faker("en_CA")

    # Generate and insert fake data for 200 people
    for _ in range(200):
        name = fake.name()
        email = fake.email()
        address = fake.street_address()
        city = fake.city()
        province = fake.province()
        bio = fake.text()
        age = random.randint(1, 100)
        created_at = datetime.now()
        updated_at = datetime.now()
        
        # Define SQL query to insert data into the people table
        insert_person_query = """
        INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        # Execute SQL query to insert data into the people table
        cur.execute(insert_person_query, (name, email, address, city, province, bio, age, created_at, updated_at))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
