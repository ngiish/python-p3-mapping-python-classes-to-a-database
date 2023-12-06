import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

# The constant CONN, that is equal to a hash that contains our connection to the database as well as a constant CURSOR that allows us to interact with the database