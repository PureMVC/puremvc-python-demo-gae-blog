"""
PureMVC Python / Google App Demo - Blog
By Nathan Levesque <nathan.levesque@puremvc.org>
Copyright(c) 2008 Nathan Levesque, Some rights reserved.
"""

import puremvc.patterns.command
import puremvc.interfaces
import vo, model, view, main

"""
Startup Commands
"""

class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, note):
        self.facade.registerProxy(model.PostProxy())

class HomeStartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, note):
        if self.facade.hasMediator(view.HomeMediator.NAME):
            self.facade.removeMediator(view.HomeMediator.NAME)
        self.facade.registerMediator(view.HomeMediator(note.getBody()))

class WriteStartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, note):
        if self.facade.hasMediator(view.WriteMediator.NAME):
            self.facade.removeMediator(view.WriteMediator.NAME)
        self.facade.registerMediator(view.WriteMediator(note.getBody()))

"""
Post Commands
"""

class AddPostCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, note):
        params = note.getBody()
        post = vo.PostVO(title = params[0],content = params[1])
        postProxy = self.facade.retrieveProxy(model.PostProxy.NAME)
        postProxy.addPost(post)
        self.sendNotification(main.AppFacade.POST_ADDED)
        
class GetPostsCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, note):
        postProxy = self.facade.retrieveProxy(model.PostProxy.NAME)
        postProxy.retrievePosts()
        self.sendNotification(main.AppFacade.POSTS_RETRIEVED)
