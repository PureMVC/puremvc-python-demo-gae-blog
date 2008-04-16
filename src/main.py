"""
PureMVC Python / Google App Demo - Blog
By Nathan Levesque <nathan.levesque@puremvc.org>
Copyright(c) 2008 Nathan Levesque, Some rights reserved.
"""

from google.appengine.ext import webapp
import wsgiref.handlers

import puremvc.patterns.facade
import controller, view

"""
Concrete Facade class implementation.
"""
class AppFacade(puremvc.patterns.facade.Facade):
	# Notification constants
	
	STARTUP            = "startup"
	HOME_STARTUP       = "homeStartup"
	WRITE_STARTUP      = "writeStartup"
	EDIT_STARTUP      = "editStartup"
	
	ADD_POST           = "addPost"	
	EDIT_POST           = "editPost"	
	DELETE_POST        = "deletePost"
	
	GET_POSTS          = "getPosts"
	POSTS_RETRIEVED    = "postsRetrieved"
	
	VIEW_WRITE_POST    = "viewWritePost"
	VIEW_EDIT_POST    = "viewEditPost"
	
	def __init__(self):
		self.initializeFacade()
		self.sendNotification(AppFacade.STARTUP)
		
	@staticmethod
	def getInstance():
		return AppFacade()
		
	def initializeFacade(self):
		super(AppFacade, self).initializeFacade()
	
		self.initializeController()
        """
        Registers commands.
        """
	def initializeController(self):
		super(AppFacade, self).initializeController()
		
		super(AppFacade, self).registerCommand(AppFacade.STARTUP, controller.StartupCommand)
		
		super(AppFacade, self).registerCommand(AppFacade.HOME_STARTUP, controller.HomeStartupCommand)
		super(AppFacade, self).registerCommand(AppFacade.WRITE_STARTUP, controller.WriteStartupCommand)
		super(AppFacade, self).registerCommand(AppFacade.EDIT_STARTUP, controller.EditStartupCommand)
		
		super(AppFacade, self).registerCommand(AppFacade.ADD_POST, controller.AddPostCommand)
		super(AppFacade, self).registerCommand(AppFacade.EDIT_POST, controller.EditPostCommand)
		super(AppFacade, self).registerCommand(AppFacade.DELETE_POST, controller.DeletePostCommand)
		
		
		super(AppFacade, self).registerCommand(AppFacade.GET_POSTS, controller.GetPostsCommand)

"""
Handles a request for the home page.
Only implements the get request as it simply displays all posts.
"""     
class HomeHandler(webapp.RequestHandler):
        facade = AppFacade.getInstance()

        """
        """
        def __init__(self):
                self.facade.sendNotification(AppFacade.HOME_STARTUP, self)
    
        def get(self):
                self.facade.sendNotification(AppFacade.GET_POSTS)

"""
Handles a request for the write page.
Get request shows the writing page.
Post request send the post to the datastore,
then redirects back to the home page.
"""  
class WriteHandler(webapp.RequestHandler):    
        facade = AppFacade.getInstance()

        def __init__(self):
                self.facade.sendNotification(AppFacade.WRITE_STARTUP, self)

        def get(self):
                self.facade.sendNotification(AppFacade.VIEW_WRITE_POST)

        def post(self):
                self.facade.sendNotification(AppFacade.ADD_POST, 
                        [self.request.get('title'),
                         self.request.get('content')])
                self.redirect("/")

"""
Handles a request for the edit page.
Get request shows the editing page.
Post request updates the post in the datastore,
then redirects back to the home page.
"""    	
class EditHandler(webapp.RequestHandler):    
        facade = AppFacade.getInstance()

        def __init__(self):
                self.facade.sendNotification(AppFacade.EDIT_STARTUP, self)

        def get(self):
                self.facade.sendNotification(AppFacade.VIEW_EDIT_POST)

        def post(self):
                self.facade.sendNotification(AppFacade.EDIT_POST, 
                        [self.request.get('key'),
                         self.request.get('title'),
                         self.request.get('content')])
                self.redirect("/")

"""
Handles a request for delete.
Get request deletes the post and redirects back to the home page.
"""  
class DeleteHandler(webapp.RequestHandler):    
        facade = AppFacade.getInstance()

        def get(self):
                self.facade.sendNotification(AppFacade.DELETE_POST, self.request.get("key"))
                self.redirect("/")


def main():
	facade = AppFacade.getInstance()

	# Steup our application and handlers
	application = webapp.WSGIApplication([('/', HomeHandler),
                                              ('/write', WriteHandler),
                                              ('/edit', EditHandler),
                                              ('/delete', DeleteHandler)],
                                              debug=True)

	# Run the application
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
	main()
