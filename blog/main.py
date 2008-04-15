"""
PureMVC Python / Google App Demo - Blog
By Nathan Levesque <nathan.levesque@puremvc.org>
Copyright(c) 2008 Nathan Levesque, Some rights reserved.
"""

from google.appengine.ext import webapp
import wsgiref.handlers

import puremvc.patterns.facade
import controller, view

class AppFacade(puremvc.patterns.facade.Facade, webapp.RequestHandler):
	
	STARTUP            = "startup"
	HOME_STARTUP       = "homeStartup"
	WRITE_STARTUP      = "writeStartup"
	
	ADD_POST           = "addPost"
	POST_ADDED         = "postAdded"
	
	GET_POSTS          = "getPosts"
	POSTS_RETRIEVED    = "postsRetrieved"
	
	VIEW_WRITE_POST    = "viewWritePost"
	
	def __init__(self):
		self.initializeFacade()
		self.sendNotification(AppFacade.STARTUP)
		
	@staticmethod
	def getInstance():
		return AppFacade()
		
	def initializeFacade(self):
		super(AppFacade, self).initializeFacade()
	
		self.initializeController()
   
	def initializeController(self):
		super(AppFacade, self).initializeController()
		
		super(AppFacade, self).registerCommand(AppFacade.STARTUP, controller.StartupCommand)
		
		super(AppFacade, self).registerCommand(AppFacade.HOME_STARTUP, controller.HomeStartupCommand)
		super(AppFacade, self).registerCommand(AppFacade.WRITE_STARTUP, controller.WriteStartupCommand)
		
		super(AppFacade, self).registerCommand(AppFacade.ADD_POST, controller.AddPostCommand)
		super(AppFacade, self).registerCommand(AppFacade.GET_POSTS, controller.GetPostsCommand)
		
	def get(self):
		pass
	
	def post(self):
		pass	

class HomeHandler(webapp.RequestHandler):
    facade = AppFacade.getInstance()
    
    def __init__(self):
        self.facade.sendNotification(AppFacade.HOME_STARTUP, self)
    
    def get(self):
        self.facade.sendNotification(AppFacade.GET_POSTS)

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

def main():
	facade = AppFacade.getInstance()
	
	application = webapp.WSGIApplication([('/', HomeHandler),
										  ('/write', WriteHandler)], debug=True)
	
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
	main()
