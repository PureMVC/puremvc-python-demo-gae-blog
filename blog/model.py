"""
PureMVC Python / Google App Demo - Blog
By Nathan Levesque <nathan.levesque@puremvc.org>
Copyright(c) 2008 Nathan Levesque, Some rights reserved.
"""

from google.appengine.ext import db
import puremvc.patterns.proxy
import vo

class PostProxy(puremvc.patterns.proxy.Proxy):
    NAME = "PostProxy"
    def __init__(self):
        super(PostProxy, self).__init__(PostProxy.NAME,[])
        
        self.data = []
    
    def getPosts(self):
        return self.data
    
    def retrievePosts(self):
        # select
        query = vo.PostVO.all()
        # Order by descending
        query.order("-datetime")
        
        self.data = []
        
        for post in query:
            self.data.append(post)
    
    def addPost(self, post):
        post.put()