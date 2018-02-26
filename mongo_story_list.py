# -*- coding: utf-8 -*-
import pymongo

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://storydb:password@ds147228.mlab.com:47228/storydb")

db = client.storydb
current_stories = db.current_stories

def get_stories():
    stories = list(current_stories.find())
    for story in stories:
        story['_id'] = str(story['_id'])
    return stories

def get_story(story_id):
    # Convert from string to ObjectId:
    object_id = ObjectId(story_id)
    story = current_stories.find_one({'_id': object_id})
    story['_id'] = str(story['_id'])
    return story

def get_story_by_key(key):
    # remove duplicates
    stories = list(current_stories.find({"book":{'$regex':key}})) + list(current_stories.find({"theme":{'$regex':key}}))
    stories_no_repeat = []
    for i in range(len(stories)):
        if stories[i] not in stories[i+1:]:
            stories_no_repeat.append(stories[i])
    for story in stories_no_repeat:
        story['_id'] = str(story['_id'])
    return stories_no_repeat

def save_story(book, theme):
    story = {"book": book, "theme": theme}
    story_id = current_stories.insert_one(story).inserted_id
    return str(story_id)

def delete_story(story_id):
    object_id = ObjectId(story_id)
    print(object_id)
    stories = current_stories.delete_one({'_id':object_id})

def update_story(story_id, book=None, theme=None):
    if book:
        update = {'$set':{'book':book}}
        object_id = ObjectId(story_id)
        current_stories.update_one({'_id':object_id}, update)
    if theme:
        update = {'$set':{'theme':theme}}
        object_id = ObjectId(story_id)
        current_stories.update_one({'_id':object_id}, update)
