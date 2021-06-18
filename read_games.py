import sqlite3

con = sqlite3.connect('games.db')
cur = con.cursor()

# Insert a row of data
for row in cur.execute("select * from games"):
    print(row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
