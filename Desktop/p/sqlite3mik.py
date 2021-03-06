# http://www.blog.pythonlibrary.org/2012/07/18/python-a-simple-step-by-step-sqlite-tutorial/

import sqlite3
 
#conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
conn = sqlite3.connect(':memory:')

cursor = conn.cursor()
 
# create a table
cursor.execute("""CREATE TABLE albums
                  (title text, artist text, release_date text, 
                   publisher text, media_type text) 
               """)
               
# insert some data
cursor.execute("INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')")
 
# save data to database
conn.commit()
 
# insert multiple records using the more secure "?" method
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()

def print_albums_by_artist():
    sql = "SELECT * FROM albums ORDER BY artist"
    cursor.execute(sql)
    print("\n\n--- Albums by artist ---\n")
    print(cursor.fetchall())  # or use fetchone()

print_albums_by_artist()

sql = """
UPDATE albums 
SET artist = 'John Doe' 
WHERE artist = 'Andy Hunter'
"""
cursor.execute(sql)
conn.commit()


print_albums_by_artist()


sql = """
DELETE FROM albums
WHERE artist = 'John Doe'
"""
cursor.execute(sql)
conn.commit()

print_albums_by_artist()

print("\n\n=== artist: Red ===\n")

sql = "SELECT * FROM albums WHERE artist=?"
cursor.execute(sql, [("Red")])
print(cursor.fetchall())  # or use fetchone()
 
print("\nHere's a listing of all the records in the table:\n")
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    print(row)
 
print("\nResults from a LIKE query:\n")
sql = """
SELECT * FROM albums 
WHERE title LIKE 'The%'"""
cursor.execute(sql)
print(cursor.fetchall())

