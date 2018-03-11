#import mock_story_list as story_list
#import mongo_story_list as story_list
import sqlite_story_list as story_list

import pytest

def setup_module():
    for story_id in [s['_id'] for s in story_list.get_stories()]:
        story_list.delete_story(story_id)

def test_get_stories():
    story_list.save_story("Test book 1", "Test theme 1")
    stories = story_list.get_stories()
    assert type(stories) is list
    for story in stories:
        for item in ['_id','book','theme']:
            assert type(story[item]) is str
        assert story['book'] == 'Test book 1'
        assert story['theme'] == 'Test theme 1'        

def test_get_story():
    stories = story_list.get_stories()
    story_id = stories[0]['_id']
    story_get = story_list.get_story(story_id)
    assert stories[0]['book'] == story_get['book']
    assert stories[0]['theme'] == story_get['theme']

def test_get_story_by_key():
    stories = story_list.get_stories()
    key1 = stories[0]['book'].split(' ')[0]
    assert type(key1) is str
    story = story_list.get_story_by_key(key1)
    assert key1 in story[0]['book']
    assert key1 in story[0]['theme']

def test_save_story():
    story_list.save_story("save book", "save theme")
    stories = story_list.get_stories()
    assert type(stories) is list
    found = False
    for story in stories:
        assert 'book' in story
        if story['book'] == "save book":
            found = True
    assert found

def test_delete_story():
    story_id = story_list.save_story("delete book", "delete theme")
    stories = story_list.get_stories()
    found = False
    for story in stories:
        if "delete" in story['book']:
            found = True 
    assert found
    story_list.delete_story(story_id)
    stories = story_list.get_stories()
    found = False
    for story in stories:
        if "delete" in story['book']:
            found = True 
    assert not found

def test_update_story():
    story_id = story_list.save_story("book before updating", "book before updating")
    story_list.update_story(story_id, book="book after updating", theme="theme after updating")
    story = story_list.get_story(story_id)
    assert "after" in story['book']
    assert "after" in story['theme']

def teardown_module():
    stories = story_list.get_stories()
    for story_id in [s['_id'] for s in stories]:
        story_list.delete_story(story_id)
