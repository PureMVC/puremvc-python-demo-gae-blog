"""
PureMVC Python / Google App Demo - Blog
By Nathan Levesque <nathan.levesque@puremvc.org>
Copyright(c) 2008 Nathan Levesque, Some rights reserved.
"""

from google.appengine.ext import db

class PostVO(db.Model):
    title = db.StringProperty(required=True)
    content = db.StringProperty(required=True)
    datetime = db.DateTimeProperty(auto_now_add=True)