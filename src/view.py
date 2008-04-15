"""
PureMVC Python / Google App Demo - Blog
By Nathan Levesque <nathan.levesque@puremvc.org>
Copyright(c) 2008 Nathan Levesque, Some rights reserved.
"""

from google.appengine.ext.webapp import template
import puremvc.patterns.mediator
import puremvc.interfaces
import model, main, vo
import os

class HomeMediator(puremvc.patterns.mediator.Mediator,
                   puremvc.interfaces.IMediator):
    NAME = "HomeMediator"
    
    templatefile = os.path.join(os.path.dirname(__file__), 'components/index.html')
    
    postProxy = None
    
    def __init__(self, viewComponent):
        super(HomeMediator, self).__init__(HomeMediator.NAME, viewComponent)
        self.postProxy = self.facade.retrieveProxy(model.PostProxy.NAME)
        
        
    def listNotificationInterests(self):
        return [main.AppFacade.POSTS_RETRIEVED]
    
    def handleNotification(self, note):
        if note.getName() == main.AppFacade.POSTS_RETRIEVED:
            template_values = {'posts': self.postProxy.getPosts()}
            self.viewComponent.response.out.write(template.render(self.templatefile, template_values))
        
        
        
class WriteMediator(puremvc.patterns.mediator.Mediator,
                    puremvc.interfaces.IMediator):
    NAME = "WriteMediator"
    
    templatefile = os.path.join(os.path.dirname(__file__), 'components/write.html')
    
    def __init__(self, viewComponent):
        super(WriteMediator, self).__init__(WriteMediator.NAME, viewComponent)
        
    def listNotificationInterests(self):
        return [main.AppFacade.POST_ADDED,
                main.AppFacade.VIEW_WRITE_POST]
    
    def handleNotification(self, note):
        if note.getName() == main.AppFacade.POST_ADDED:
            self.viewComponent.redirect("/")
        if note.getName() == main.AppFacade.VIEW_WRITE_POST:
            self.viewComponent.response.out.write(template.render(self.templatefile,{}))
