# -*- coding: utf-8 -*-

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from bottle import get, post, run, debug, default_app, request, template, static_file, redirect

#import mock_story_list as story_list
#import mongo_story_list as story_list
import sqlite_story_list as story_list

@get('/')
@get('/story-list')
def get_story_list():
    stories = story_list.get_stories()
    for story in stories:
        book = story['book']
        theme = story['theme']
    output = template('story_list.tpl', stories=stories)
    return output

@post('/new-story')
def post_new_story():
    theme = request.forms.theme
    book = request.forms.book
    story_list.save_story(theme, book)
    redirect('/')

@get('/discard-story/<id>')
def get_discard_story(id):
    story_list.delete_story(id)
    redirect('/')

@post('/search-results')
def get_search_results():
    key = request.POST.key.strip()
    stories = story_list.get_story_by_key(key)
    if stories == key:
        return template('not_found.tpl', key=key)
    return template('story_list.tpl', stories=stories)

@get('/edit-story/<id>')
def get_edited_story(id):
    edit_story = story_list.get_story(id)
    return template('edit_story.tpl', story = edit_story)
    

@post('/edit-story/<id>')
def post_edited_story(id):
    theme = request.forms.new_theme
    book = request.forms.new_book
    story_list.update_story(id, theme, book)
    redirect('/')

@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

def setup():
    story_list.save_story('book1', '中文')
    story_list.save_story('book2', 'theme2')
    story_list.save_story('book3', 'theme3')
    story_list.save_story('book4', 'theme4')

#setup()
#debug(True)
#run(host='localhost', port=8080, reloader=True)
application = default_app()