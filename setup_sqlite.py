import sqlite3

conn = sqlite3.connect('story.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE Stories(book TEXT, theme TEXT)")
    cur.execute("INSERT INTO Stories VALUES('book1', 'theme1')")
    cur.execute("INSERT INTO Stories VALUES('book2', 'theme2')")

if conn:
    conn.close()