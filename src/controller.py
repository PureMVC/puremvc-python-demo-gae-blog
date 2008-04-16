"""
PureMVC Python / Google App Demo - Blog
By Nathan Levesque <nathan.levesque@puremvc.org>
Copyright(c) 2008 Nathan Levesque, Some rights reserved.
"""

import puremvc.patterns.command
import puremvc.interfaces
import vo, model, view, main

"""
Startup Command

Executed when the C{AppFacade} first instantiates.
"""
class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
        def execute(self, note):
                self.facade.registerProxy(model.PostProxy())

"""
Home Startup Command
Executed when the home page is requested and the C{HomeHandler} is instantiated.
"""
class HomeStartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
        def execute(self, note):
                if self.facade.hasMediator(view.HomeMediator.NAME):
                        self.facade.removeMediator(view.HomeMediator.NAME)
                self.facade.registerMediator(view.HomeMediator(note.getBody()))

"""
Write Startup Command

Executed when the write page is requested and the C{HomeHandler} is instantiated.
"""
class WriteStartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
        def execute(self, note):
                if self.facade.hasMediator(view.WriteMediator.NAME):
                        self.facade.removeMediator(view.WriteMediator.NAME)
                self.facade.registerMediator(view.WriteMediator(note.getBody()))

"""
Edit Startup Command

Executed when the edit page is requested and the C{HomeHandler} is instantiated.
"""
class EditStartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
        def execute(self, note):
                if self.facade.hasMediator(view.EditMediator.NAME):
                        self.facade.removeMediator(view.EditMediator.NAME)
                self.facade.registerMediator(view.EditMediator(note.getBody()))

"""
Add Post Command

Adds the post to the datastore via the C{PostProxy}.
"""

class AddPostCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
        def execute(self, note):
                postProxy = self.facade.retrieveProxy(model.PostProxy.NAME)

                params = note.getBody()

                post = vo.PostVO(title = params[0],content = params[1])

                postProxy.addPost(post)

"""
Edit Post Command

Edits an existing post in the datastore via the C{PostProxy}.
"""     
class EditPostCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
        def execute(self, note):
                postProxy = self.facade.retrieveProxy(model.PostProxy.NAME)

                params = note.getBody()
                key = params[0] 
                title = params[1]
                content = params[2]

                postProxy.editPost(key, title, content)

"""
Delete Post Command

Deletes an existing post in the datastore via the C{PostProxy}.
"""           
class DeletePostCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
        def execute(self, note):
                postProxy = self.facade.retrieveProxy(model.PostProxy.NAME)
                key = note.getBody()
                postProxy.deletePost(key)

"""
Get Posts Command

Uses the C{PostProxy} to get a list of all posts.
"""            
class GetPostsCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
        def execute(self, note):
                postProxy = self.facade.retrieveProxy(model.PostProxy.NAME)
                postProxy.retrievePosts()
                self.sendNotification(main.AppFacade.POSTS_RETRIEVED)

