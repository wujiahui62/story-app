# sqlite story list module
# use complete path when using it on pythonanywhere
import sqlite3
connection = sqlite3.connect('story.db')

def get_stories():
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, book, theme FROM Stories")
    return [{'_id':str(i), 'book':b, 'theme':t} for (i, b, t) in cursor.fetchall()]


def get_story(story_id):
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, book, theme FROM Stories WHERE rowid = " + story_id)
    items = [{'_id': str(i), 'book': b, 'theme':t} for (i, b, t) in cursor.fetchall()]
    if len(items) == 1:
        item = items[0]
        return item
    return None

def get_story_by_key(key):
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, book, theme from Stories WHERE book like ? or theme like ?", ('%'+key+'%', '%'+key+'%'))
    items = [{'_id': str(i), 'book': b, 'theme':t} for (i, b, t) in cursor.fetchall()]
    if(len(items) > 0):
        return items
    return None

def save_story(book, theme):
    cursor = connection.cursor()
    inserted = (book, theme)
    cursor.execute('INSERT INTO Stories VALUES(?, ?)', inserted)
    lastrowid = cursor.lastrowid
    connection.commit()
    return str(lastrowid)

def delete_story(story_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Stories where rowid = " + story_id)
    connection.commit()

def update_story(story_id, book=None, theme=None):
    cursor = connection.cursor()
    if book:
        cursor.execute("UPDATE Stories SET book = ? WHERE rowid = " + story_id, (book,))
    if theme:
        cursor.execute("UPDATE Stories SET theme = ? WHERE rowid = " + story_id, (theme,))
