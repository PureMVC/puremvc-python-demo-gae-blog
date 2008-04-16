"""
PureMVC Python / Google App Demo - Blog
By Nathan Levesque <nathan.levesque@puremvc.org>
Copyright(c) 2008 Nathan Levesque, Some rights reserved.
"""

from google.appengine.ext import db

"""
Post value object. Derives from db.Model so that it can be
stored in the database.
"""
class PostVO(db.Model):
    # Title as a required string property
    title = db.StringProperty(required=True)

    # Content as a required string property
    content = db.StringProperty(required=True)
    
    # Datetime as a DateTime property that gets automatically set to
    # the current time whenever the post is added/updated
    datetime = db.DateTimeProperty(auto_now=True)
