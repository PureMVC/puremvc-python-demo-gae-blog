"""
PureMVC Python / Google App Demo - Blog
By Nathan Levesque <nathan.levesque@puremvc.org>
Copyright(c) 2008 Nathan Levesque, Some rights reserved.
"""

from google.appengine.ext import db
import puremvc.patterns.proxy
import vo

"""
Proxy for managing creation, editing and deletion of posts.
"""
class PostProxy(puremvc.patterns.proxy.Proxy):
        NAME = "PostProxy"
        def __init__(self):
                super(PostProxy, self).__init__(PostProxy.NAME,[])
                
                self.data = []

        def getPosts(self):
                return self.data

        """
        Retrieves an array of all C{PostVO} objects from the datastore in descending order
        """
        def retrievePosts(self):
                # Select all
                query = vo.PostVO.all()
                
                # Order by datetime descending
                query.order("-datetime")

                # Clear data
                self.data = []

                # Query is executed when looped through
                for post in query:
                        self.data.append(post)

        """
        Adds a given C{PostVO} to the datastore.
        """
        def addPost(self, post):
                post.put()

        """
        Edits a C{PostVO} in the datastore by the unique key of the post and the updated title and content.
        """
        def editPost(self, key, title, content):
                # Get the post with the unique key that matches
                post = vo.PostVO.get(key)

                # Assign vars
                post.title = title
                post.content = content

                # Update it in the datastore
                post.put()

        """
        Deletes a post from the datastore by its unique key.
        """
        def deletePost(self, key):
                # Get the post with the unique key that matches
                post = vo.PostVO.get(key)

                # Delete it
                post.delete()
