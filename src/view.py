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
                return [main.AppFacade.VIEW_WRITE_POST]

        def handleNotification(self, note):
                if note.getName() == main.AppFacade.VIEW_WRITE_POST:
                        self.viewComponent.response.out.write(template.render(self.templatefile,{}))
            
class EditMediator(puremvc.patterns.mediator.Mediator,
                   puremvc.interfaces.IMediator):
        NAME = "EditMediator"

        templatefile = os.path.join(os.path.dirname(__file__), 'components/edit.html')

        def __init__(self, viewComponent):
                super(EditMediator, self).__init__(EditMediator.NAME, viewComponent)

        def listNotificationInterests(self):
                return [main.AppFacade.VIEW_EDIT_POST]

        def handleNotification(self, note):
                if note.getName() == main.AppFacade.VIEW_EDIT_POST:
                        key = self.viewComponent.request.get("key")
                        post = vo.PostVO.get(key)
                        template_values = {'post': post}
                        self.viewComponent.response.out.write(template.render(self.templatefile,template_values))
