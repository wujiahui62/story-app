# sqlite story list module
# use complete path when using it on pythonanywhere
import sqlite3
connection = sqlite3.connect('story.db')

def get_stories():
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, theme, book FROM Stories")
    return [{'_id':str(i), 'theme':b, 'book':t} for (i, b, t) in cursor.fetchall()]


def get_story(story_id):
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, theme, book FROM Stories WHERE rowid = " + story_id)
    items = [{'_id': str(i), 'theme': b, 'book':t} for (i, b, t) in cursor.fetchall()]
    if len(items) == 1:
        item = items[0]
        return item
    return None

def get_story_by_key(key):
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, theme, book from Stories WHERE book like ? or theme like ?", ('%'+key+'%', '%'+key+'%'))
    items = [{'_id': str(i), 'theme': b, 'book':t} for (i, b, t) in cursor.fetchall()]
    if(len(items) > 0):
        return items
    return key

def save_story(theme, book):
    cursor = connection.cursor()
    inserted = (theme, book)
    cursor.execute('INSERT INTO Stories VALUES(?, ?)', inserted)
    lastrowid = cursor.lastrowid
    connection.commit()
    return str(lastrowid)

def delete_story(story_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Stories where rowid = " + story_id)
    connection.commit()

def update_story(story_id, theme=None, book=None):
    cursor = connection.cursor()
    if book:
        cursor.execute("UPDATE Stories SET book = ? WHERE rowid = " + story_id, (book,))
    if theme:
        cursor.execute("UPDATE Stories SET theme = ? WHERE rowid = " + story_id, (theme,))
