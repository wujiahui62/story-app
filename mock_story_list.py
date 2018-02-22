# mock story list module

current_stories = []

current_id = 0

def get_stories():
    return current_stories

def get_story(story_id):
    for story in current_stories:
        if story['_id'] == story_id:
            return story
    return None

def get_story_by_key(key):
    stories = []
    for story in current_stories:
        if story['theme'] == key or story['book'] == key:
            stories.append(story)
    return stories


def save_story(book, theme):
    global current_id
    current_id += 1
    story_id = str(current_id)
    story = {'_id': story_id,
            'book': book,
            'theme': theme
    }
    current_stories.append(story)
    return story_id

def delete_story(story_id):
    global current_stories
    current_stories = [ story for story in current_stories if story['_id'] != story_id]

def update_story(story_id, book=None, theme=None):
    for story in current_stories:
        if story['_id'] == story_id:
            if book:
                story['book'] = book
            if theme:
                story['theme'] = theme