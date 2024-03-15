import sqlite3
import inspect
import os

def main():
  # Determine the path of the database
  global db_path
  script_dir = get_script_dir()
  db_path = os.path.join(script_dir, 'music_library.db')

  # Create the database
  create_music_db()

  # Add some albums to the database
  add_album_to_db('Up To Here', 'The Tragically Hip', 1989)
  add_album_to_db('Fully Completely', 'The Tragically Hip', 1992)
  add_album_to_db('Day For Night', 'The Tragically Hip', 1994)
  add_album_to_db('Trouble at the Henhouse', 'The Tragically Hip', 1996)
  add_album_to_db('Phantom Power', 'The Tragically Hip', 1998)
  add_album_to_db('Presto', 'Rush', 1989)
  add_album_to_db('Roll the Bones', 'Rush', 1991)
  add_album_to_db('Counterparts', 'Rush', 1993)
  add_album_to_db('Test for Echo', 'Rush', 1996)
  add_album_to_db('Curb', 'Nickelback', 1996)
  add_album_to_db('The State', 'Nickelback', 2000)
  add_album_to_db('Silver Side Up', 'Nickelback', 2001)

  album_id = get_album_id_from_db('Test for Echo', 'Rush', 1996)
  if album_id != 0:
    print(f'Album ID from DB is {album_id}')
  else:
    print('Albumb not found!')

  album_id = get_album_id_from_db('Test for Echo', 'Rush', 1982)
  if album_id != 0:
    print(f'Album ID from DB is {album_id}')
  else:
    print('Album not found!')

  fetched_albums = get_90s_albums()

  for album in fetched_albums:
    print(f'{album[1]} - {album[0]} : {album[2]}')
  
  return

def get_script_dir():
  """Determines the path of the directory in which this script resides
  Returns:
    str: Full path of the directory in which this script resides
  """

  script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
  return os.path.dirname(script_path)

def create_music_db():

  # Open a connection to the database.
  con = sqlite3.connect(db_path)

  # Get a Cursor object that can be used to run SQL queries on the database.
  cur = con.cursor()

  # Define an SQL query that creates a table named 'albums'.
  # Each row in this table will hold information about a specific album.
  create_album_table_query = """
    CREATE TABLE IF NOT EXISTS albums
    (
      id INTEGER PRIMARY KEY,
      title TEXT NOT NULL,
      artist TEXT NOT NULL,
      year INTEGER NOT NULL
    );
  """

  # Execute the SQL query to create the 'albums' table.
  # Database operations like this are called transactions.
  cur.execute(create_album_table_query)

  # Commit (save) pending transactions to the database.
  # Transactions must be committed to be persistent.
  con.commit()

  # Close the database connection.
  # Pending transactions are not implicitly committed, so any
  # pending transactions that have not been committed will be lost. 
  con.close()

  print(f'Created the database {db_path}')

def add_album_to_db(title, artist, year):
  # Check whether album is already in the DB
  album_id = get_album_id_from_db(title, artist, year)
  if album_id != 0:
    return album_id

  con = sqlite3.connect(db_path)
  cur = con.cursor()

  # Define an SQL query that inserts a row of data in the albums table.
  # The ?'s are placeholders can be fill in when the query is executed.
  # Specific values can be passed as a tuple into the execute() method.
  add_album_query = """
    INSERT INTO albums
    (
      title,
      artist,
      year
    )
     VALUES (?, ?, ?);
  """
  # Define tuple of data for new album to insert into albums table
  # Data values must be in same order as specified in query
  new_album = (
    title,
    artist,
    year)

  # Execute query to add new album to albums table
  cur.execute(add_album_query, new_album)
  con.commit()
  con.close()

  print(f'Added Album {title} by {artist} from year {year} to DB as album # {cur.lastrowid}')

  # Return the ID of the added record
  return cur.lastrowid

def get_album_id_from_db(title, artist, year):

  con = sqlite3.connect(db_path)
  cur = con.cursor()

  # Define query to search for album in DB
  find_album_query = """
    SELECT id FROM albums
    WHERE title = ? AND artist = ? AND year = ?
  """

  # Define tuple of data for album to search for in albums table
  # Data values must be in same order as specified in query
  album_info = (title, artist, year)

  # Execute query to add new album to albums table
  cur.execute(find_album_query, album_info)
  query_result = cur.fetchone()
  con.close()

  # Return the album ID if album is present in the DB
  if query_result is not None:
    return query_result[0]

  # Return 0 if album is not present in the DB
  return 0

def get_90s_albums():
  con = sqlite3.connect(db_path)
  cur = con.cursor()

  # Define query
  get_90s_albums_query = """
    SELECT title, artist, year FROM albums
    WHERE year < 2000 AND year >= 1990;
  """

  # Execute query
  cur.execute(get_90s_albums_query)
  query_result = cur.fetchall()
  con.close()

  return query_result

if __name__ == '__main__':
  main()
