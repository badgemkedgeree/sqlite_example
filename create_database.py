import sqlite3

con = sqlite3.connect('games.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE games
               (name text, rank int)''')

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
