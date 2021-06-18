import sqlite3

from model.Game import Game

con = sqlite3.connect('games.db')
cursor = con.cursor()

minecraft = Game("Minecraft", 1)
minecraft.save(cursor)
roblox = Game("Roblox", 2)
roblox.save(cursor)

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
